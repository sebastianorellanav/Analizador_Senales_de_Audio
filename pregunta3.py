import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np

#Entrada: frecuencia del audio, datos del sonido
#Salida: tranformada de fourier, array con frecuencias
#Descripcion:
def calcularTransformada(freq, datos):
    y = fourier.fft(datos)
    y =fourier.fftshift(y)
    y = np.abs(y)
    freqs = np.fft.fftfreq(len(y),1/freq)
    freqs = fourier.fftshift(freqs)

    return freqs, y

#Entrada:array de frecuencias (eje X), transformada de fourier (eje y)
#Salida: no hay return, La función crea un grafico que sera mostrado mas adelante
#DEscripcion: La función grafica la transformada de fourier en funcion de la frecuencia
def graficarTransformadaFrecuencia(freqs, transf):
    plt.figure(figsize=(30, 4))
    plt.fill_between(freqs,transf)
    plt.title('Transformada de Fourier: Amplitud vs frecuencia(Hz)')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    plt.savefig("transformadaFourier.png")

#Entrada: frecuencia de audio,datos del sonido
#Salida: transformada de fourier inversa, array de tiempos
#Descripción: calculo de la transformada de fourier inversa
def calcularTransformadaInversa(freq,datos): 
    y = fourier.fft(datos)
    inversa = fourier.ifft(y)
    tiempos = np.arange(len(datos))/float(freq)
    return tiempos, inversa

#Entrada: arreglos de tiempos (eje x), transformada de fourier (eje y)
#Salida: imagen del gráfico amplitud vs tiempo obtenido de la serie de fourier inversa
#Descripcion: 
def graficarTransformadaInversa(tiempos,inversa):
    plt.figure(figsize=(30, 4))
    plt.fill_between(tiempos, inversa.real,inversa.imag,color="green")
    plt.xlim(tiempos[0], tiempos[-1])
    plt.title('Transformada de Fourier inversa: Amplitud vs Tiempo(s)')
    plt.xlabel('tiempo (s)')
    plt.ylabel('Amplitud')
    plt.savefig("transformadaFourierInversa.png")

#Entrada: datos del sonido, transformada inversa del sonido
#Salida: array de errores simples, error cuadratico medio
#Descripción: la funcion calcula el error absoluto entre cada uno de los
#             valores de las funciones. Además calcula el error cuadratico medio
def calcularError(sonido,inversa):
    errores = []
    for i in range(len(sonido)):
        dif = sonido[i] - inversa[i]
        dif = abs(dif)
        errores.append(dif)

    mse = ((sonido - inversa)**2).mean(axis=None)
    rmse = mse**(1/2)
    
    return errores, rmse

#Entrada: arreglos de tiempos (eje x), arreglo de errores (eje y), error cuadratico medio
#Salida: gráfico error absoluto vs tiempo 
#Descripcion: 
def graficarError(tiempos, errores,rmse):
    plt.figure(figsize=(30,4))
    plt.fill_between(tiempos, errores)
    plt.title('Error Sonido Original y Transformada Iversa')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Error Absoluto')
    