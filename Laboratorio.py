###########################################################################################################
#######---------------------------------------------------------------------------------------------#######
#######                                   Laboratorio 1 Redes                                       #######
#######---------------------------------------------------------------------------------------------#######
#######                                   Sebastian Orellana                                        #######
#######                                      Franco Tapia                                           #######
#######                                                                                             #######
#######                                        version 1                                            #######
#######---------------------------------------------------------------------------------------------#######
#######                                       descripcion                                           #######
###########################################################################################################
#0. Librerias utilizadas

import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np


#1.Lea una señal de audio y determine a qué corresponde cada uno de los parámetros retornados.

#Entrada: string con nombre de archivo
#Salida: muestreo: frecuencia de datos por segundo
#        sonido: contiene datos del sonido
#Descripción: leer archivo con señal de sonido
def leerSenal(nombre):
   
    muestreo, sonido = waves.read(nombre)
    return muestreo, sonido

#Entrada: muestreo y sonido
#Salida: gráfico que representa audio leido
#Descripción: graficar señal de audio obtenida
def graficar(muestreo,sonido):
    tiempo = np.arange(len(sonido))/float(muestreo)
    plt.figure(figsize=(30, 4))
    plt.fill_between(tiempo, sonido,color="green")
    plt.xlim(tiempo[0], tiempo[-1])
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.show()


# Llamado a funciones en pregunta 1
muestreo, sonido = leerSenal('handel.wav')
graficar(muestreo,sonido)


#2.Grafique la función de audio en el tiempo.


#3.Calcule la transformada de Fourier de la señal de audio:
#a.Grafique la señal en el dominio de la frecuencia.
#b.Al resultado del punto 3, calcule la transformada de Fourier inversa.
#c.Compare con la señal leída en el punto 1.


#4.Calcule y grafique el espectrograma de la función. ​El espectrograma permite visualizar información en el 
#dominio de la frecuencia y del tiempo a la vez. Note que requiere un gráfico de tres dimensiones (t, f, |fft|)
# o una imagen


#Filtre el ruido de la señal de audio leía en el punto 1, para ello:
#a.Diseñe un filtro FIR para eliminar el ruido de la señal de audio. Determine el tipo de filtro
#(pasabajos,pasaaltos,o pasabanda) y determine las frecuencias de corte para este, ver Figura 2.
#b.Pruebe distintos parámetros al momento de aplicar el filtro.
#c.Obtenga la transformada de Fourier y el espectrograma de la señal filtrada y analice sus resultados.
