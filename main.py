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
import scipy.io.wavfile as waves
import numpy as np
import pregunta1 as pregunta1
import pregunta2 as pregunta2
import pregunta3 as pregunta3
import pregunta4 as pregunta4
import pregunta6 as pregunta6
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

#6.a. Filtre el ruido de la señal de audio con un Filtro FIR
taps = 100			#numero de pulsos
cutoff = 1000		#frecuencia de corte
filtrado_1 = pregunta6.lowPassFilter(sonido, freq, taps, cutoff, 0) #filtrar soonido
waves.write('filtrado_1.wav', freq, filtrado_1.astype(np.int16))  #guardar audio filtrado_1

#b.Pruebe distintos parámetros al momento de aplicar el filtro.
taps = 200			#numero de pulsos
cutoff = 500		#frecuencia de corte
filtrado_2 = pregunta6.lowPassFilter(sonido, freq, taps, cutoff, 0) #filtrar soonido
waves.write('filtrado_2.wav', freq, filtrado_2.astype(np.int16))  #guardar audio filtrado_2

taps = 80			#numero de pulsos
cutoff = 2000		#frecuencia de corte
filtrado_3 = pregunta6.lowPassFilter(sonido, freq, taps, cutoff, 0) #filtrar soonido
waves.write('filtrado_3.wav', freq, filtrado_3.astype(np.int16))  #guardar audio filtrado_3

#Mostrar Graficos
otros.mostrarGraficos()
