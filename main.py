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
pregunta2.graficarSonidoTiempo(freq,sonido,"Señal de Audio: Amplitud vs Tiempo (s)")

#3.Calcule la transformada de Fourier de la señal de audio:
freqs, transf = pregunta3.calcularTransformada(freq, sonido)

#3.a.Grafique la señal en el dominio de la frecuencia.
nombreGrafico = 'Transformada de Fourier: Amplitud vs frecuencia(Hz)'
pregunta3.graficarTransformadaFrecuencia(freqs, transf,nombreGrafico)

#b.Al resultado del punto 3, calcule la transformada de Fourier inversa.
tiempos, inversa = pregunta3.calcularTransformadaInversa(freq, sonido)
pregunta3.graficarTransformadaInversa(tiempos, inversa)

#c.Compare con la señal leída en el punto 1
errores, rmse = pregunta3.calcularError(sonido, inversa)
pregunta3.graficarError(tiempos, errores, rmse)
print(rmse)

#4. graficar Espectrograma
nombreGrafico = 'Espectograma de señal de audio'
pregunta4.graficarEspectrograma(sonido,freq,nombreGrafico)

#6.a. Filtre el ruido de la señal de audio con un Filtro FIR
taps = 200			#numero de pulsos
cutoff = 1700		#frecuencia de corte
filtrado_1 = pregunta6.lowPassFilter(sonido, freq, taps, cutoff, 0) #filtrar soonido
waves.write('filtrado_1.wav', freq, filtrado_1.astype(np.int16))  #guardar audio filtrado_1
pregunta2.graficarSonidoTiempo(freq,filtrado_1,"Señal de Audio Filtrada: Amplitud vs Tiempo (s)")

#b.Pruebe distintos parámetros al momento de aplicar el filtro.

cutoff = 850		#frecuencia de corte
filtrado_2 = pregunta6.lowPassFilter(sonido, freq, taps, cutoff, 0) #filtrar soonido
waves.write('filtrado_2.wav', freq, filtrado_2.astype(np.int16))  #guardar audio filtrado_2

cutoff = 500		#frecuencia de corte
filtrado_3 = pregunta6.lowPassFilter(sonido, freq, taps, cutoff, 0) #filtrar soonido
waves.write('filtrado_3.wav', freq, filtrado_3.astype(np.int16))  #guardar audio filtrado_3

#c. Obtenga la transformada de Fourier y el espectograma de la señal filtrada
freqs_filtrado, transf_filtrado = pregunta3.calcularTransformada(freq, filtrado_1)

#Transformada de Fourier señal filtrada
nombreGrafico = 'Transformada de Fourier señal filtrada: Amplitud vs frecuencia(Hz)'
pregunta3.graficarTransformadaFrecuencia(freqs, transf_filtrado,nombreGrafico)

#Espectograma filtrado
nombreGrafico = 'Espectograma de señal de audio filtrado'
pregunta4.graficarEspectrograma(filtrado_1,freq,nombreGrafico)




otros.mostrarGraficos()
