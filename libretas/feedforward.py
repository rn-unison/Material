# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Modulo con las funciones de feedforward
para ser usadas con la libreta de jupyter
backpropagation.ipynb

"""

__author__ = "Julio Waissman Vilanova"
__date__ = "17 de septiembre de 2017"


import numpy as np
import pickle


def inicializa_red_neuronal(capas, neuronas_por_capa, tipo_salida):
    """
    Inicializa una red neuronal como un diccionario de datos.  Se
    asume en este caso que la función de activación es la función
    logística

    Parametros
    ----------
    capas: Un número entero con el número total de capas.
           Minimo 3 (una de entrada, una oculta, una de salida).

    neuronas_por_capa: Una lista de enteros donde el primer
                       elemento es el número de entradas y el último
                       el número de salidas, mientras que los
                       intermedios son el númerode neuronas en
                       cada capa oculta.

    tipo: Un string entre {'lineal', 'logistica', 'softmax'}
          con el tipo de función de salida de la red.

    Devuelve
    --------
    Un diccionario `rn` tal que
        - rn['capas'] = capas
        - rn['nxc'] = neuronas_por_capas
        - rn['tipo'] = tipo
        - rn['W'] = lista de matrices de parámetros, cuyo primer elemento 
                    es `None`, de manera que rn['W'][l] son los pesos de
                    la capa l.
        - rn['medias'] = lista de medias de cada atributo
                         (se inicializan con puros 0)
        - rn['std'] = lista de desviaciones estandard de cada atributo
                      (se inicializan con puros 1)

    """
    if capas != len(neuronas_por_capa):
        raise ValueError('`capas` no es consistente con `nxc`')
    if tipo_salida not in ('lineal', 'logistica', 'softmax'):
        raise ValueError('No se dispone de esta salida')
    rn = {'capas': capas, 'nxc': neuronas_por_capa, 'tipo': tipo_salida}
    rn['medias'] = np.zeros(neuronas_por_capa[0])
    rn['std'] = np.ones(neuronas_por_capa[0])
    rn['W'] = ([None] +
               [(2*np.random.random((nl, nla + 1)) - 1)/np.sqrt(nla)
                for (nla, nl)
                in zip(neuronas_por_capa[:-1], neuronas_por_capa[1:])])

    return rn


def obtiene_medias_desviaciones(x):
    """
    Obtiene las medias y las desviaciones estandar atributo a atributo.

    Parametros
    ----------
    @param x: un ndarray de dimensión (T, n) donde T es el número de
              elementos y n el número de atributos

    @return: medias, desviaciones donde ambos son ndarrays de
             dimensiones (n,) con las medias y las desviaciones
             estandar respectivamente.

    """
    return x.mean(axis=0), x.std(axis=0)


def normaliza(x, medias, desviaciones):
    """
    Normaliza los datos x

    Parametros
    ----------
    x: un ndarray de dimensión (T, n) donde T es el número
       de elementos y n el número de atributos

    medias: ndarray de dimensiones (n,) con las medias
            con las que se normalizará

    desviaciones: ndarray de dimensiones (n,) con
                  las desviaciones con las que se normalizará

    Devuelve
    --------
    un ndarray de las mismas dimensiones de x pero normalizado.

    Ejemplo
    -------


    """
    return (x - medias) / desviaciones


def logistica(z):
    """
    Calcula la función logística para cada elemento de z

    Parametros
    ----------
    z: un ndarray

    Devuelve
    --------
    un ndarray de las mismas dimensiones que z

    Ejemplo
    -------
    
    """
    return 1 / (1 + np.exp(-z))


def softmax(z):
    """
    Calculo de la regresión softmax

    Parametros
    ----------
    z: ndarray de dimensión (T, K) donde z[i, :] es el vector
       de aportes lineales de el objeto i

    Devuelve
    --------
    un ndarray de dimensión (T, K) donde cada columna es el
    calculo softmax de su respectivo vector de entrada.

    Ejemplo
    -------
    
    """
    e = np.exp(z - z.max())
    return e / e.sum(axis=0)


def extendida(matriz):
    """
    Agrega un renglon de unos a una matriz

    """
    return np.r_[np.ones((1, matriz.shape[1])), matriz]


def feedforward(X, red_neuronal):
    """
    Calcula la salida estimada para los valores de `X` utilizando
    red_neuronal

    Parametros
    ----------
    X: ndarray de shape (T, n) donde T es el número de ejemplos
       y n el número de atributos

    red_neuronal: Estructura de datos de una red neuronal inicializada
                  con la función `inicializa_red_neuronal`

    Devuelve
    --------
    Una lista de `ndarray` de activaciones por cada capa donde
    `Y_est` (la salida) es el último elemento de la lista transpuesto.

    """
    Xn = normaliza(X, red_neuronal['medias'], red_neuronal['std'])
    A = [Xn.T]

    for Wl in red_neuronal['W'][1:-1]:
        Z = Wl.dot(extendida(A[-1]))
        A.append(logistica(Z))

    Z = red_neuronal['W'][-1].dot(extendida(A[-1]))

    A.append(Z if red_neuronal['tipo'] is 'lineal' else
             logistica(Z) if red_neuronal['tipo'] is 'logistica' else
             softmax(Z))
    return A


def perdida_red(Y, X, rn):
        """
        Calcula la función de perdida de una red neuronal,
        de acuerdo al tipo de salida y a un conjunto de datos
        conocidos expresados por Y y X

        Parametros
        ----------
        Y: un ndarray de dimension (T, K) con los valores de salida

        X: un ndarray de dimension (T, N) con los valores de entrada

        rn: Una red neuronal como la definimos a partir de un diccionario

        Devuelve
        --------
        Un número flotante con el valor de pérdida

        """
        A = feedforward(X, rn)
        Y_est = A[-1].T
        return perdida(Y, Y_est, rn['tipo'])


def perdida(Y, Y_est, tipo):
    """
    Calcula la función de perdida de una red neuronal,
    de acuerdo al tipo de salida.

    Parametros
    ----------
    Y: un ndarray de dimension (T, K), con los valores de salida

    Y_est: un ndarray de dimension (T, K), con los valores de salida estimados

    tipo: Un string que puede ser 'lineal', 'logistica' o 'softmax'

    Devuelve
    --------
    Un número flotante con el valor de pérdida

    """
    return (np.square(Y - Y_est).sum() / (2 * Y.shape[0])
            if tipo is 'lineal' else
            -(np.log(Y_est[Y == 1]).sum() +
              np.log(1 - Y_est[Y == 0]).sum()) / Y.shape[0]
            if tipo is 'logistica' else
            -np.log(Y_est[Y == 1]).mean())


def guarda_rn(archivo, rn):
    """
    Guarda una red neuronal en el archivo "archivo".
    Si el archivo existe, sera reemplazado sin
    preguntas, al puro estilo mafioso.

    Parametros
    ----------
    archivo: string con el nombre de un archivo (aunque no exista)

    rn: Un diccionario tipo red neuronal como lo definimos

    """
    with open(archivo, 'wb') as arch:
        pickle.dump(rn, arch, -1)
        arch.close()


def carga_rn(archivo):
    """
    Carga una red neuronal de un archivo

    Parametros
    ----------
    archivo: string con el nombre de un archivo tipo pickle

    Devuelve
    --------
    Una red neuronal

    """
    with open(archivo, 'rb') as arch:
        rn = pickle.load(arch)
        arch.close()
        return rn
