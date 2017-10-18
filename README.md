
# El libro de texto sobre aprendizaje profundo

[Deep Learning (I. Goodfellow, Yoshua Bengio y Aaron Courville),
2016](http://www.deeplearningbook.org "EL LIBRO de Aprendizaje
Profundo")

Este libro se edito por *MIT Press*, pero la editorial permitió a los
autores subir el material en linea de forma gratuita. La única
condición que puso la editorial es que solo se puede consultarlo
directamente en la red, por lo que su formato o es fácilmente
traducible a pdf u otros formatos. Es considerado desde hace 3 años
que se puso en linea el primer borrador como la biblia del aprendizaje
profundo.

# Redes neuronales

#### Presentaciones

- [Introducción a las redes neuronales](presentaciones/intro_rn.pdf)

#### Prácticas a desarrollar

- [Libreta de *Jupyter* (Kernel Python 3.X) para practicar el algoritmo de *feedforward* ](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/Redes%20neuronales%20hacia%20adelante.ipynb)

# Aprendizaje

#### Presentaciones

- [Presentación de Geoffrey Hinton sobre aprendizaje en una neurona](presentaciones/aprendizaje_una_neurona.pdf)

- [Presentación sobre aprendizaje en varias neuronas](presentaciones/aprendizaje_red_neuronal.pdf)


#### Lecturas (artículos, tutoriales, ...)

- [El artículo original donde se propone el algoritmo de *back-propagation*](articulos/Learning-representations-by-back-propagating-errors.pdf)

- [Un artículo muy bueno sobre *b-prop* y consejos útiles](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

- [Una página que explica muy claramente las unidades *softmax* y su aprendizaje](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/)

#### Prácticas a desarrollar

- [Libreta de *Jupyter* (Kernel 3.X) sobre aprendizaje de una neurona de salida lineal.](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/neurona%20lineal.ipynb)

- [Libreta de *Jupyter* (Kernel 3.X) sobre aprendizaje de una neurona de salida logística.](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/neurona%20logistica.ipynb)

- [Libreta de *Jupyter* (Kernel 3.X) sobre aprendizaje de una unidad de salida *softmax*.](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/unidad%20softmax.ipynb)

- [Libreta de *Jupyter* (Kernel 3.X) sobre el algoritmo de *backpropagation*.](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/backpropagation.ipynb)

# Arquitecturas profundas (en general)

#### Presentaciones

- [Una presentación introductoria de *deep learning* por Y. LeCun (NYU/Facebook)](http://cilvr.cs.nyu.edu/lib/exe/fetch.php?media=deeplearning:dl-intro.pdf)

- [Una guia para seleccionar arquitecturas profundas y su ajuste](http://www.deeplearningbook.org/slides/11_practical.pdf)

- [Presentación sobre generalización y curvas de aprendizaje en arquitecturas profundas](http://www.deeplearningbook.org/slides/05_ml.pdf)


# Plataformas de desarrollo


## Tensorflow

[Tensorflow](https://www.tensorflow.org) es una biblioteca dinámica de
computo numérico basado en el concepto de grafos de flujo de
datos. *Tensorflow* se desarrolló inicialmente por el grupo de
investigación en aprendizaje máquina de *Google research* y poco a
poco se va convirtiendo en el medio más popular para el desarrollo de
algoritmos de *DL*.

#### Lecturas (artículos, tutoriales, ...)

- [Tutoriales básicos de *Tensorflow* (muy claros)](https://www.tensorflow.org/get_started/)

#### Prácticas a desarrollar

- [Libreta de *Jupyter* (Kernel 3.X) para entender el funcionamiento básico de *Tensorflow* (1.3 o más reciente)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/intro_tensorflow.ipynb)
- [Libreta de *Jupyter* (Kernel 3.X) para entender como programar una red neuronal hacia adelante sencilla en *Tensorflow* (1.3 o más reciente)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/tensorflow_red_simple.ipynb)

## PyTorch

[PyTorch](http://pytorch.org) es una plataforma relativamente nueva, y
qye junto a *Tensorflow* mandaron al venerable *Theano* (pionero de
los entornos para aprendizaje profundo) al retiro. PyTorch es basado
100% en python a diferencia de *Tensorflow* el cual precompila en una
plataforma externa. Una vez definida una red, *PyTorch* construye el
grafo de operaciones *on the fly* (no se cual es la traducción
correcta de este término, y *en el aire* no representa lo que quiere
decir a mi entender).

#### Lecturas (artículos, tutoriales, ...)

- [Ejemplos de uso de *PyTorch*](http://pytorch.org/tutorials/beginner/pytorch_with_examples.html#)


## Keras

[Keras](https://keras.io) es un modulo de *Python* que ofrece un marco
general de desarrollo de soluciones a problemas con aprendizaje
profundo el cual es independiente de la plataforma de resolución por
gráfos de operaciones. *Keras* es una interface común pars
*Tensorflow*, *Theano* y otras plataformas.

#### Lecturas (artículos, tutoriales, ...)

- [Curso gratuito de *DL* para desarrolladores, basado en Keras](http://course.fast.ai/index.html)

# Redes convolucionales

#### Presentaciones

- [Una presentación introductoria de redes convolucionales](presentaciones/conv_nets.pdf)


# Redes recurrentes

#### Presentaciones

- [Una presentación introductoria de redes recurrentes (de G. Hitton)](presentaciones/redes_recurrentes.pdf)
