import matplotlib.pyplot as plt

#Entrada: datos del sonido y frecuencia del audio 
#Salida: gráfico que representa el espetrograma del audio
#Descripción: graficar el espectrograma
def graficarEspectrograma(sonido, freq):
	plt.figure(figsize=(30, 4))
	plt.specgram(sonido, NFFT=512, Fs=freq)
	plt.colorbar()
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')