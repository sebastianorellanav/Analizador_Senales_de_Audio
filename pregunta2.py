import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np

#Entrada: frecuencia del audio y datos del sonido
#Salida: gráfico que representa audio leido
#Descripción: graficar señal de audio obtenida
def graficarSonidoTiempo(freq,sonido):
    tiempo = np.arange(len(sonido))/float(freq)
    plt.figure(figsize=(30, 4))
    plt.fill_between(tiempo, sonido,color="green")
    plt.xlim(tiempo[0], tiempo[-1])
    plt.title('Señal de audio: Amplitud vs Tiempo (s)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.savefig("funcionAudioTiempo.png")