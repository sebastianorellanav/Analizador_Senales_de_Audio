###########################################################################################################
#######---------------------------------------------------------------------------------------------#######
#######                                   Laboratorio 1 Redes                                       #######
#######---------------------------------------------------------------------------------------------#######
#######                                   Sebastian Orellana                                        #######
#######                                      Franco Tapia                                           #######
#######                                                                                             #######
#######                                        version 3                                            #######
#######---------------------------------------------------------------------------------------------#######
#######                                       descripcion                                           #######
###########################################################################################################

###########################################################################################################
#######									   Librerias                                                #######
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy import signal
import numpy as np
import pregunta1 as pregunta1
import pregunta2 as pregunta2
import pregunta3 as pregunta3
import pregunta4 as pregunta4
import otros as otros


#1.Lea una señal de audio y determine a qué corresponde cada uno de los parámetros retornados.
freq, sonido = pregunta1.leerSenal('handel.wav')  #primer parametro = frecuencia del audio
									    #segundo parametro = datos del sonido

#2 Grafique la función de audio en el tiempo.
pregunta2.graficarSonidoTiempo(freq,sonido)

#3.Calcule la transformada de Fourier de la señal de audio:
freqs, transf = pregunta3.calcularTransformada(freq, sonido)

#3.a.Grafique la señal en el dominio de la frecuencia.
pregunta3.graficarTransformadaFrecuencia(freqs, transf)

#b.Al resultado del punto 3, calcule la transformada de Fourier inversa.
tiempos, inversa = pregunta3.calcularTransformadaInversa(freq, sonido)
pregunta3.graficarTransformadaInversa(tiempos, inversa)

#c.Compare con la señal leída en el punto 1
errores, rmse = pregunta3.calcularError(sonido, inversa)
pregunta3.graficarError(tiempos, errores, rmse)
print(rmse)

#4. graficar Espectrograma
pregunta4.graficarEspectrograma(sonido,freq)

#Mostrar Graficos
otros.mostrarGraficos()
