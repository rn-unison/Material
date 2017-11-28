#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
prog_din.py
------------

Algoritmos de programación dinámica

"""

__author__ = 'juliowaissman'

import random


def actualiza_valor(mdp, valor_pi, s0, a, descuento):
    """
    Función de ayuda para calcular

    $sum_{s_1 \in S} p(s_0, a, s_1) ( r(s_0, a, s_1) + \gamma V^{\pi}(s_1)$

    lo que se usa tanto para la mejora de polítca como para el calculo de la política

    :param mdp: Un objeto tipo mdp.MDP
    :param valor_pi: La función de valor-estado para la política pi
    :param s0: Un estado de mdp (el estado en el tiempo t)
    :param a: Una acción legal en s (de acuerdo a mdp)
    :param descuento: El factor de descuento 0.0 <= descuento <= 1.0

    :return Un flotante que resuelve la ecuación anterior

    """
    return sum(mdp.p(s0, a, s1) * (mdp.r(s0, a, s1) + descuento * valor_pi[s1]) for s1 in mdp.estados)


def calculo_politica_determinista(mdp, politica, descuento, epsilon, valor_ini=None):
    """
    Calculo del valor de una política utilizando iteraciones

    :param mdp: Un objeto tipo mdp.mdp
    :param politica: Una política determinista (un diccionario donde pi[s] = a)
    :param descuento: El factor de descuento (0.0 <= descuento <= 1.0)
    :param epsilon; Criterio para acabar las iteraciones (valor positivo muy pequeño)
    :valor_ini: Valores iniciales de la función de acción-valor, en forma de
                diccionario, donde ``valor_ini[estado]`` es el valor estimado de ``estado``

    :return: Un diccionario ``valor``, tal que ``valor[s]`` es el valor del estado s

    """
    if valor_ini is None:
        valor_ini = {estado: 0 for estado in mdp.estados}
    valor = valor_ini.copy()
    max_var = epsilon + 1

    while epsilon < max_var:
        max_var = 0
        for estado in mdp.estados:
            nv = actualiza_valor(mdp, valor, estado, politica[estado], descuento)
            max_var = max(max_var, abs(valor[estado] - nv))
            valor[estado] = nv
    return valor


def iteracion_politica(mdp, descuento, epsilon, visible=False):
    """
    Programación dinámica en MDPs con estados y acciones finitas, utilizando el clásico (e ineficiente) método
    de iteración de política (con calculo de la política en forma iterativa).

    :param mdp: Un objeto tipo mdp.mdp
    :param descuento: El factor de descuento (0.0 <= descuento <= 1.0)
    :param epsilon; Criterio para acabar las iteraciones en la iteración de política (valor positivo muy pequeño)
    :param vidible: Si True, entonces despliega en consola cada modificación de la política.

    :return: Un diccionario ``politica``, tal que ``politica[s]`` es la acción a realizar en el estado ``s`` bajo
             una política óptima determinista.

    """
    diff = True
    valor_pi = None
    politica = {estado: random.choice(mdp.a_legales(estado)) for estado in mdp.estados}

    while diff:
        if visible:
            print(politica)
        diff = False
        valor_pi = calculo_politica_determinista(mdp, politica, descuento, epsilon, valor_pi)
        for estado in mdp.estados:
            a = max(mdp.a_legales(estado), key=lambda accion: actualiza_valor(mdp, valor_pi, estado, accion, descuento))
            if a != politica[estado]:
                diff = True
                politica[estado] = a
    return politica


if __name__ == '__main__':


    # El ejemplo del inventario para un caso muy simple que es fácil hacer a mano.
    from inventario import Inventario
    modelo = Inventario(m=10, b=0, max_dem=10, a_max=10, primero=True, c=(0, 1, 1, 0), gu=3, demanda=None)
    pi = iteracion_politica(modelo, descuento=0.99, epsilon=0.001, visible=True)
    print("La política óptima con PD")
    print("estado".center(10) + "|" + "accion".center(10))
    for s in sorted(pi.keys()):
        print(str(s).center(10) + '|' + str(pi[s]).center(10))
