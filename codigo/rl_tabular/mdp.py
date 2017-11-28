#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mdp.py
------------


"""

__author__ = 'juliowaissman'


import random


class MDP(object):
    """
    MDP: Una clase abstracta para porcesos de desición markovianos
    ===============================================================

    Clase para modelar un proceso de decisión markiviano con un conjunto
    de estados finitos y acciones finitas.

    Un proceso de desición markoviano está definido por (S, A, p, r)  donde:

    S: Conjunto de estados.

    A: Conjunto de acciones, donde self.a_legales(s) es el conjunto de acciones
       legales en el estado s.

    p\:SxAxS -> R: Probabilidad de transición del estado s al estado s' al
                   aplicar la acción a.

    r\:SxAxS --> R: Recompensa inmediata esperada de pasar del estado s al
                    estado s' al aplicar la acción a.

    """
    def __init__(self, estados=frozenset()):
        """
        Constructor, inicializa variables

        @param estados: conjunto finito de estados (default el conjunto vacio)

        """
        self.estados = estados

    def a_legales(self, s):
        """
        Encuentra el conjunto de acciones admisibles para un estado particular s

        @param s: Un estado valido del proceso

        @return: Un conjunto de acciones

        """
        if s not in self.estados:
            raise ValueError("El estado " + str(s) + "no es un estado válido")

    def r(self, s, a, sp):
        """
        Calcula el refuerzo de aplicar la acción a en el estado s, llevando al estado sp

        @param s: estado del proceso
        @param a: accion admisible en el estado s
        @param sp: estado del proceso

        @return un valor numérico que si es positivo es un recompensa y negativo un castigo

        """
        if s not in self.estados or sp not in self.estados or a not in self.a_legales(s):
            raise ValueError("Alguno de los valores de entrada no es válido")

    def p(self, s, a, sp):
        """
        Calcula la probabilidad de pasar del estado s al estado sp utilizando la acción a.

        @param s: estado del proceso
        @param a: accion admisible en el estado s
        @param sp: estado del proceso

        @return: Un flotante y, 0.0 <= y <= 1.0

        """
        if s not in self.estados or sp not in self.estados or a not in self.a_legales(s):
            raise ValueError("Alguno de los valores de entrada no es válido")


class MDPsim(object):
    """
    Clase para modelar una simulación de procesos que asumimos de desición markovianos.

    @param

    """
    def es_estado(self, s):
        """
        Verifica que s sea un estado válido

        @param s: Una lista o un np.ndarray

        @return: True si s es un estado válido

        """
        raise NotImplementedError()

    def a_legales(self, s):
        """
        Encuentra el conjunto de acciones admisibles para un estado particular s

        @param s: Un estado valido del proceso

        @return: Un conjunto de acciones

        """
        if not self.es_estado(s):
            raise ValueError("El estado " + str(s) + "no es un estado válido")

    def transicion(self, s, a):
        """
        Realiza una transición en el proceso.

        @param s: Un estado del sistema
        @param a: Una accion legal en s

        @return: sp, r donde s es un estado legal del sistema y r es la recompensa inmediata

        """
        if not self.es_estado(s) or a not in self.a_legales(s):
            raise ValueError("Alguno de los valores de entrada no es válido")


