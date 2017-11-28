#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

El problema del inventario
==========================

Los problemas de Inventario son un tipo de problema ejemplo muy comun
en control estocástico. En este modulo se considera en este caso un
inventario con las siguientes características:

- ``m`` es la máxima capacidad de almacenamiento (default ``m = 10000``)

- ``b`` es la capacidad de *backlogging*, esto es, de surtir fuera de almacen
  (default B = 0)

- ``max_dem``es la demanda máxima esperada por el producto en un periodo de
  tiempo

- Las ventas se realizan en unidades (los estados y las acciones son números
  enteros)

- La decisión de cuantos items comprar (acciones) se realizan al inicio del
  periodo de tiempo

- Los pedidos (acciones) tienen un máximo ``A_max``
  (default ``A_max = maxint``)

- Las acciones admisibles en el estado ``s`` son
  A(s) = {0, ... , min(M + B - s, A_max)}

- Si la demanda excede el inventario y el *backlogging*, se pierden las ventas.

- La demanda es una variable aleatoria que se genera a partir de una
  distribución ``demanda(x)`` Si no se especifica ``demanda(x)``, por default
  se utiliza una distribución uniforme entre 0 y ``M + B``. Para este problema
  se considera la demanda estacionaria, por lo que su distribución no cambia en
  el tiempo.

- El pedido se puede surtir inmediatamente (``primero=True``, por default) o al
  final del periodo de tiempo (``primero=False``), en el primer caso se
  considera la venta a lo largo del periodo de tiempo, y en el otro se considera
  que en el periodo de tiempo se levantan los pedidos y se surte inmediatamente
  que llega la mercancia.

- La variación del inventario está dada por ``sp = max( -B, s + a - venta )``

- La ``venta`` es un valor entre 0 y s + a + B si se surte primero y s + B si se
  surte al final

- La probabilidad de sp es

    + 0 si ``sp > s + a``(imposible que haya mas de lo que se tenía mas lo que
    se pidió).

    + demanda(venta) si ``sp > -B``

    + suma de ``demanda(x)`` para ``x`` de ``s + a + B`` hasta ``s + a + B +
    max_dem`` (la suma de la probabilidad de haber podido vender mas de lo que
    teníamos en almacen para venta).

- El costo se toma dependiendo de Primero,

    Si ``primero=True`` entonces

        costo(s, a) = c_0 * int(a > 0) + c_1 * a + c_2 * max(0, s + a - B) + c_3
        * max(0, B - s - a)

    Si ``primero=False``

        costo(s, a) = c_0 * int(a > 0) + c_1 * a + c_2 * max(0, s - B) + c_3 *
        max(0, B - s)

    donde:

    + c_0 = Costo de emitir un pedido
    + c_1 = Costo unitario de la mercancía
    + c_2 = Costo de almacenaje por unidad en el periodo de tiempo
    + c_3 = Costo de backlogging por unidad en el periodo de tiempo

- La ganancia se obtiene como ganancia(s, a, sp) = gu * venta,  donde gu es la
  ganancia unitaria.

- La recomprensa es r(s, a, sp) = ganancia(s, a, sp) - costo(s, a)

"""

import mdp
import random


class Inventario(mdp.MDP):
    """
    Clase para el problema de inventario descrito en la explicación
    general del módulo

    :param m: máxima capacidad de almacenamiento, default maxint

    :param b: capacidad de "backlogging (surtir fuera de almacen), default 0

    :param max_dem: máxima demanda esperada en un periodo de tiempo

    :param a_max: máximo número de items en un solo pedido, default maxint

    :param primero: si True el pedido se surte inmediatamente, si False,
                    el pedido se surte al final del día

    :param c: (c1, c2, c3, c4) donde

              + c1 es el coto de emitir un pedido,
              + c2 es el costo unitario,
              + c3 es el costo unitario de almacenaje y
              + c4 es el costo unitario de backlogging,

    :param gu: ganancia unitaria

    :param demanda: Función que calcula la probabilidad de una demanda
                    de x items, por default se utiliza una
                    ditribución uniforme entre $0$ y $M+B$.
    """

    def __init__(self, m=10000, b=0, max_dem=1000, a_max=10000,
                 primero=True, c=(0, 1, 1, 0), gu=1, demanda=None):
        """

        :param m: máxima capacidad de almacenamiento (default maxint)

        :param b: capacidad de "backlogging, esto es de surtir fuera de almacen (default 0)

        :param max_dem: máxima demanda esperada en un periodo de tiempo

        :param a_max: máximo número de items en un solo pedido (default maxint)

        :param primero: si True el pedido se surte inmediatamente, si False, el pedido se surte al final del día

        :param c: (c1, c2, c3, c4) donde

                  + c1 es el coto de emitir un pedido,
                  + c2 es el costo unitario,
                  + c3 es el costo unitario de almacenaje y
                  + c4 es el costo unitario de backlogging,

        :param gu: ganancia unitaria

        :param demanda: Función que calcula la probabilidad de una demanda de x items, por default se utiliza una
                        ditribución uniforme entre $0$ y $max_dem$.
        """
        self.m = m
        self.b = b
        self.max_dem = max_dem
        self.a_max = a_max
        self.primero = primero
        self.c = c
        self.gu = gu
        if not demanda:
            self.demanda = lambda x: 1.0 / (max_dem + 1)
        else:
            self.demanda = demanda
        super(Inventario, self).__init__(set(range(-self.b, self.m + 1)))

    def a_legales(self, s):
        """
        Las acciones admisibles en el estado ``s`` son A(s) = {0, ... , min(m + b - s, a_max)}

        :param s: estado válido
        :return: lista de acciones admisibles

        """
        return range(0, min(self.m + self.b - s, self.a_max) + 1)

    def p(self, s, a, sp):
        """
        - La variación del inventario está dada por ``sp = max( -B, s + a - venta )``

        - La ``venta`` es un valor entre 0 y s + a + B si se surte primero y s + B si se surte al final

        - La probabilidad de sp es
            + 0 si ``sp > s + a``
            + demanda(venta) si ``sp > -b``
            + suma de ``demanda(x)`` para ``x`` de ``s + a + b`` hasta ``s + a + b + max_dem``

        :param s: estado
        :param a: accion admisible en s
        :param sp: estado

        :return: Un número flotante entre 0 y 1

        """
        a_p = 0 if self.primero else 1
        venta = s + a - sp
        if -self.b + a_p * a < sp <= s + a:
            return self.demanda(venta)
        elif sp == -self.b + a_p * a:
            return sum(self.demanda(x) for x in range(venta, self.max_dem + 1))
        else:
            return 0


    def r(self, s, a, sp):
        """
        Si ``primero=True`` entonces
            costo(s, a) = c[0] * int(a > 0) + c[1] * a + c[2] * max(0, s + a - B) + c[3] * max(0, B - s - a)
        Si ``primero=False``
            costo(s, a) = c[0] * int(a > 0) + c[1] * a + c[2] * max(0, s - B) + c[3] * max(0, B -s)

        La ganancia se obtiene como ganancia(s, a, sp) = gu * venta,  donde gu es la ganancia unitaria.

        La recomprensa es r(s, a, sp) = ganancia(s, a, sp) - costo(s, a)

        :param s: estado
        :param a: accion admisible en s
        :param sp: estado

        :return: Un número
        """
        a_p = a if self.primero else 0
        costo = self.c[0] * int(a > 0) + \
            self.c[1] * a + \
            self.c[2] * max(0, s + a_p - self.b) + \
            self.c[3] * max(0, self.b - s - a_p)
        ganancia = self.gu * (s + a_p - sp)
        return ganancia - costo


class InventarioSim(mdp.MDPsim):
    """
    Clase para simular elproblema de inventario descrito en la explicación general del módulo

    :param m: máxima capacidad de almacenamiento (default maxint)

    :param b: capacidad de "backlogging, esto es de surtir fuera de almacen (default 0)

    :param max_dem: máxima demanda esperada en un periodo de tiempo

    :param a_max: máximo número de items en un solo pedido (default maxint)

    :param primero: si True el pedido se surte inmediatamente, si False, el pedido se surte al final del día

    :param c: (c1, c2, c3, c4) donde

              + c1 es el coto de emitir un pedido,
              + c2 es el costo unitario,
              + c3 es el costo unitario de almacenaje y
              + c4 es el costo unitario de backlogging,

    :param gu: ganancia unitaria

    :param venta: Función que calcula la probabilidad de una demanda de x items, por default se utiliza una
                    ditribución uniforme entre $0$ y $M+B$.
    """

    def __init__(self, m=10000, b=0, max_dem=1000, a_max=10000,
                 primero=True, c=(0, 1, 1, 0), gu=3, venta=None):
        """
        Constructor

        """
        self.m = m
        self.b = b
        self.max_dem = max_dem
        self.a_max = a_max
        self.primero = primero
        self.c = c
        self.gu = gu
        if not venta:
            self.venta = lambda estado: random.randint(0, self.max_dem)
        else:
            self.venta = venta
        self.estados = range(-self.b, self.m + 1)

    def es_estado(self, s):
        return s in range(-self.b, self.m + 1)

    def estado_inicial(self):
        return random.choice(self.estados)

    def a_legales(self, s):
        """
        Las acciones admisibles en el estado ``s`` son ``A(s) = {0, ... , min(m + b - s, a_max)}``

        :param s: estado válido
        :return: lista de acciones admisibles

        """
        return range(0, min(self.m + self.b - s, self.a_max) + 1)

    def transicion(self, s, a):
        if self.primero:
            sp = max(-self.b, s + a - self.venta(s))
        else:
            sp = max(-self.b, s - self.venta(s)) + a
        return sp, self.r(s, a, sp)

    def r(self, s, a, sp):
        """
        Si ``primero=True`` entonces
            costo(s, a) = c[0] * int(a > 0) + c[1] * a + c[2] * max(0, s + a - B) + c[3] * max(0, B - s - a)
        Si ``primero=False``
            costo(s, a) = c[0] * int(a > 0) + c[1] * a + c[2] * max(0, s - B) + c[3] * max(0, B -s)

        La ganancia se obtiene como ganancia(s, a, sp) = gu * venta,  donde gu es la ganancia unitaria.

        La recomprensa es r(s, a, sp) = ganancia(s, a, sp) - costo(s, a)

        :param s: estado
        :param a: accion admisible en s
        :param sp: estado

        :return: Un número
        """
        a_p = a if self.primero else 0
        costo = self.c[0] * int(a > 0) + \
            self.c[1] * a + \
            self.c[2] * max(0, s + a_p - self.b) + \
            self.c[3] * max(0, self.b - s - a_p)
        ganancia = self.gu * (s + a_p - sp)
        return ganancia - costo


if __name__ == '__main__':

    ejemplo = Inventario(m=10, b=1, max_dem=5, a_max=10, primero=True, c=(0, 1, 1, 0), gu=10, demanda=None)
    print("Descripción de probabilidades de transición del mpd del inventario")
    for s in ejemplo.estados:
        for a in ejemplo.a_legales(s):
            for sp in ejemplo.estados:
                if ejemplo.p(s, a, sp) > 0:
                    print("p(" + str(s) + ', ' + str(a) + ', ' + str(sp) + ') = ' + str(ejemplo.p(s, a, sp)))

    modelo = InventarioSim(m=10, b=0, max_dem=10, a_max=14, primero=True, c=(0, 1, 1, 0), gu=3, venta=None)
    print("Simulación con politica aleatoria de el modelo de simulación")
    print('Paso'.center(10) + 's'.center(5) + 'a'.center(5) + "s'".center(5) + "r". center(5))
    s = modelo.estado_inicial()
    for paso in range(10):
        a = random.choice(modelo.a_legales(s))
        sp, r = modelo.transicion(s, a)
        print(str(paso).center(10) + str(s).center(5) + str(a).center(5) + str(sp).center(5) + str(r).center(5))
        s = sp
