import matplotlib.pyplot as plt

#Entrada: datos del sonido y frecuencia del audio 
#Salida: gráfico que representa el espetrograma del audio
#Descripción: graficar el espectrograma
def graficarEspectrograma(sonido, freq,nombreGrafico):
	plt.figure(figsize=(10, 4))
	plt.specgram(sonido, NFFT=512, Fs=freq)
	plt.colorbar()
	plt.title(nombreGrafico)
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')
	plt.savefig(nombreGrafico + ".png")