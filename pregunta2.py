import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np

#Entrada: frecuencia del audio y datos del sonido
#Salida: gráfico que representa audio leido
#Descripción: graficar señal de audio obtenida
def graficarSonidoTiempo(freq,sonido,nombreArchivo):
    tiempo = np.arange(len(sonido))/float(freq)
    plt.figure(figsize=(10, 4))
    plt.fill_between(tiempo, sonido)
    plt.xlim(tiempo[0], tiempo[-1])
    plt.title(nombreArchivo)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.savefig(nombreArchivo+".png")