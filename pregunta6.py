from scipy import signal

#Entrada:  Señal original, frecuencia, Nº de taps para usar en el filtro, 
#          Frecuencia de Corte para el filtro, A lo largo de qué eje aplicar 
#          el filtrado de pasa bajo.
#Salida: señal filtrada pasa bajo con la misma dimension que la original
#Descripcion:
def lowPassFilter(data, fs, nfilt=80, fw_base=4000, axis=0):
    # La frecuencia de Nyquist de la señal es la mitad de la frecuencia de muestreo
    nyq_freq = fs / 2.0

    # Se utiliza un FIR filter con un Hamming window.
    filt = signal.firwin(nfilt, cutoff=fw_base / nyq_freq, window='hamming')

    # Use lfilter para filtrar con el filtro FIR.
    # Filtramos a lo largo de la segunda dimensión porque eso representa el tiempo
    filtered_sound = signal.filtfilt(filt, [1.0], data, axis=axis)

    return filtered_sound


