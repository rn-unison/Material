#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
rl_tabular.py
------------


"""

__author__ = 'juliowaissman'


import random


def politica_epsilon_voraz(q, s, lista_a, epsilon):
    return (random.choice(lista_a)
            if random.random() < epsilon else
            max(lista_a, key=lambda a: q[(s, a)]))


def sarsa0(entorno, descuento, egreedy, alpha, max_episodios, max_pasos):

    visitados = set([])
    q = {}

    for _ in range(max_episodios):             # Por cada episodio

        s = entorno.estado_inicial()            # Estado inicial del episodio
        lista_a = entorno.a_legales(s)
        if s not in visitados:
            for a in lista_a:
                q[(s, a)] = 0.1 * random.random()
            visitados.add(s)
        a = politica_epsilon_voraz(q, s, lista_a, egreedy)

        for _ in range(max_pasos):             # Por cada paso en el episodio

            # Simulación
            sp, r = entorno.transicion(s, a)
            lista_ap = entorno.a_legales(sp)
            if len(lista_ap) == 0:
                q[(s, a)] += alpha * (r - q[(s, a)])
                break
            if sp not in visitados:
                for ap in lista_ap:
                    q[(sp, ap)] = 0.1 * random.random()
                visitados.add(sp)
            ap = politica_epsilon_voraz(q, sp, lista_ap, egreedy)

            # Aprendizaje por refuerzo
            inc_q = r + descuento * q[(sp, ap)] - q[(s, a)]
            q[(s, a)] += alpha * inc_q

            # Actualización y criterio de fin de episodio
            s = sp
            a = ap

    # Regresa la política
    return {s: max([a for a in entorno.a_legales(s)],
                   key=lambda ac: q[(s, ac)])
            for s in visitados}


def qlearning0(entorno, descuento, egreedy, alpha, max_episodios, max_pasos):

    visitados = set([])
    q = {}

    for _ in range(max_episodios):             # Por cada episodio
        s = entorno.estado_inicial()            # Estado inicial del episodio
        lista_a = entorno.a_legales(s)
        if s not in visitados:
            for a in lista_a:
                q[(s, a)] = 0.1 * random.random()
            visitados.add(s)

        for _ in range(max_pasos):             # Por cada paso en el episodio

            a = politica_epsilon_voraz(q, s, lista_a, egreedy)
            sp, r = entorno.transicion(s, a)
            lista_a = entorno.a_legales(sp)
            if len(lista_a) == 0:
                q[(s, a)] += alpha * (r - q[(s, a)])
                break
            if sp not in visitados:
                for ap in lista_a:
                    q[(sp, ap)] = 0.1 * random.random()
                visitados.add(sp)

            inc_q = r + descuento * max(q[(sp, ap)]
                                        for ap in lista_a) - q[(s, a)]
            q[(s, a)] += alpha * inc_q
            s = sp

    # Regresa la política
    return {s: max([a for a in entorno.a_legales(s)],
                   key=lambda ac: q[(s, ac)])
            for s in visitados}


if __name__ == '__main__':

    # El ejemplo del inventario para un caso que es fácil hacer a mano.
    from inventario import InventarioSim
    modelo = InventarioSim(m=10, b=0, max_dem=10, a_max=10,
                           primero=True, c=(0, 1, 1, 0), gu=3)

    print("Ejemplo con SARSA")
    pi = sarsa0(modelo, descuento=0.99, egreedy=0.1, alpha=0.1,
                max_episodios=1000, max_pasos=1000)
    print("estado".center(10) + "|" + "accion".center(10))
    for s in sorted(pi.keys()):
        print(str(s).center(10) + '|' + str(pi[s]).center(10))

    print("Ejemplo con Q-Learning")
    pi = qlearning0(modelo, descuento=0.99, egreedy=0.1, alpha=0.4,
                    max_episodios=1000, max_pasos=1000)
    print("estado".center(10) + "|" + "accion".center(10))
    for s in sorted(pi.keys()):
        print(str(s).center(10) + '|' + str(pi[s]).center(10))
