<p><center><img src="rn2.png" width="200" /></center></p>

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

# Introducción y preliminares

#### Presentaciones

- [Introducción a las redes neuronales](presentaciones/intro_rn.pdf)

#### Lecturas (artículos, tutoriales, ...)

- [Una introducción a la probabilidad (por Arian Maleki and Tom Do de Stanford)](articulos/cs229-prob.pdf)

#### Prácticas a desarrollar

- Libreta de *Jupyter* (Python 3.X): practica de `numpy` y `matplotlib`[(ver)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/intro_numpy.ipynb) [(descargar)](libretas/intro_numpy.zip).


# Redes neuronales

#### Presentaciones

- [Presentación de Geoffrey Hinton sobre aprendizaje en una neurona](presentaciones/aprendizaje_una_neurona.pdf)

- [Presentación sobre aprendizaje en varias neuronas](presentaciones/aprendizaje_red_neuronal.pdf)


#### Lecturas (artículos, tutoriales, ...)

- [El artículo original donde se propone el algoritmo de *back-propagation*](articulos/Learning-representations-by-back-propagating-errors.pdf)

- [Un artículo muy bueno sobre *b-prop* y consejos útiles](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)

- [Una página que explica muy claramente las unidades *softmax* y su aprendizaje](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/)


#### Prácticas a desarrollar

- Libreta de *Jupyter* (Python 3.X): aprendizaje de una neurona lineal [(ver)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/neurona_lineal.ipynb) [(descargar)](libretas/neurona_lineal.zip).

- Libreta de *Jupyter* (Python 3.X): aprendizaje de una neurona logística [(ver)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/neurona_logistica.ipynb) [(descargar)](libretas/neurona_logistica.zip).

- Libreta de *Jupyter* (Python 3.X): aprendizaje de una unidad softmax [(ver)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/unidad_softmax.ipynb) [(descargar)](libretas/unidad_softmax.zip).

- Libreta de *Jupyter* (Python 3.X): redes hacia adelante [(ver)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/redes_neuronal_hacia_adelante.ipynb) [(descargar)](libretas/redes_neuronal_hacia_adelante.zip).



# Arquitecturas profundas (en general) y plataformas de desarrollo

#### Plataformas de desarrollo

- [Tensorflow](https://www.tensorflow.org) es una biblioteca dinámica
  de computo numérico basado en el concepto de grafos de flujo de
  datos. *Tensorflow* se desarrolló inicialmente por el grupo de
  investigación en aprendizaje máquina de *Google research* y poco a
  poco se va convirtiendo en el medio más popular para el desarrollo
  de algoritmos de *DL*.


- [PyTorch](http://pytorch.org) es una plataforma relativamente nueva,
  y que junto a *Tensorflow* mandaron al venerable *Theano* (pionero
  de los entornos para aprendizaje profundo) al retiro. PyTorch es
  basado 100% en python a diferencia de *Tensorflow* el cual
  precompila en una plataforma externa. Una vez definida una red,
  *PyTorch* construye el grafo de operaciones *on the fly* (no se cual
  es la traducción correcta de este término, y *en el aire* no
  representa lo que quiere decir a mi entender).

- [Keras](https://keras.io) es un modulo de *Python* que ofrece un
  marco general de desarrollo de soluciones a problemas con
  aprendizaje profundo el cual es independiente de la plataforma de
  resolución por gráfos de operaciones. *Keras* es una interface común
  pars *Tensorflow*, *Theano* y otras plataformas.


#### Presentaciones

- [Una presentación introductoria de *deep learning* por Y. LeCun (NYU/Facebook)](http://cilvr.cs.nyu.edu/lib/exe/fetch.php?media=deeplearning:dl-intro.pdf)

- [Una guia para seleccionar arquitecturas profundas y su ajuste](http://www.deeplearningbook.org/slides/11_practical.pdf)

- [Presentación sobre generalización y curvas de aprendizaje en arquitecturas profundas](http://www.deeplearningbook.org/slides/05_ml.pdf)



#### Lecturas (artículos, tutoriales, ...)

- [Un artículo sobre lo que todavía no se puede hacer con *deep learning*](articulos/dl_critical.pdf)

- [Tutoriales básicos de *Tensorflow* (muy claros)](https://www.tensorflow.org/get_started/)

- [Ejemplos de uso de *PyTorch*](http://pytorch.org/tutorials/beginner/pytorch_with_examples.html#)

- [Curso gratuito de *DL* para desarrolladores, basado en PyTorch](http://course.fast.ai/index.html)


#### Prácticas a desarrollar

- Libreta de *Jupyter* (Python 3.X): conceptos básicos de TensorFlow  [(ver)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/intro_tensorflow.ipynb) [(descargar)](libretas/intro_tensorflow.zip).

- Libreta de *Jupyter* (Python 3.X): red neuronal sencilla en TensorFlow  [(ver)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/tensorflow_red_simple.ipynb) [(descargar)](libretas/tensorflow_red_simple.zip).


# Redes convolucionales

#### Presentaciones

- [Una presentación introductoria de redes convolucionales](presentaciones/conv_nets.pdf)

- [Una presentación sobre transferencia de estilo en imagenes utilizando redes neuronales convolucionales](presentaciones/style_transfer.pdf)

#### Lecturas (artículos, tutoriales, ...)

- [El artículo original de *style transfer* de Gatty *et. al*, 2016, en versión libre](articulos/style_transfer.pdf)

- [Página de *Github* con lo necesario para poder implementar *Style Transfer* con TensorFlow](https://www.anishathalye.com/2015/12/19/an-ai-that-can-mimic-any-artist/)

#### Prácticas a desarrollar

- [Libreta de *Jupyter* (Kernel 3.X) para crear un modelo de CNN en *Tensorflow* (1.3 o más reciente)](https://github.com/curso-redes-neuronales-unison/Material/blob/master/libretas/red_convolucional_simple.ipynb)



# Redes recurrentes

#### Presentaciones

- [Una presentación introductoria de redes recurrentes (de G. Hitton)](presentaciones/redes_recurrentes.pdf)

#### Lecturas (artículos, tutoriales, ...)

- [Un excelente artículo sobre redes tipo LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Redes recurrentes para la generación de texto](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)


#### Prácticas a desarrollar


# Aprendizaje por refuerzo profundo

#### Presentaciones

- [Una presentación inicial sobre aprendizaje por refuerzo (presentación mía viejita)](presentaciones/rl_intro.pdf)
- [Unas notas sobre aprendizaje por refuerzo con pseudocódigo](presentaciones/rl_ideas.pdf)

#### Lecturas (artículos, tutoriales, ...)

- [Una presentación muy buena de `Deep RL` de Standford](presentaciones/deep_rl_stanford.pdf)
- [Una presentación muy completa (y algo difícil) de *Deepmind*](presentaciones/deep_rl_deepmind.pdf)
- [Una serie de posts sobre Deep RL de A. Juliani, enfocados a su implementación en *TensorFlow*](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)
- [El tutorial de Karpahty sobre DRL](http://karpathy.github.io/2016/05/31/rl/)

#### Prácticas a desarrollar

<!---
- [Archivos en python para aprendizaje reforzado tipo tabular](codigo/rl_tabular)

-->
