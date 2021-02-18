from scipy.signal import firwin,remez, kaiser_atten, kaiser_beta,freqz,firls,filtfilt,butter,sosfilt,lfilter
import numpy as np
import matplotlib.pyplot as plt

def bandpass_remez(ntaps, lowcut, highcut, fs, width):
    delta = 0.5 * width
    edges = [0, lowcut-delta,lowcut + delta,highcut - delta, highcut + delta, 0.5*fs]
    taps=remez(ntaps,edges,[0, 1, 0],Hz=fs)
    return taps

def plot_response(fs,w,h,title):
     "Utility function to plot response functions"
     fig = plt.figure()
     ax = fig.add_subplot(111)
     r=0.5*fs*w/np.pi
     rr=100*np.log10(np.abs(h))
     '''
     gain=[]
     freq=[]
     for i in range(len(rr)):
       if rr[i]>=-12 and rr[i]<=12:
          gain.append(rr[i])
          freq.append(r[i])
     gain=np.array(gain)
     freq=np.array(freq)
     '''
     ax.plot(r,rr)
     ax.set_ylim(-15,15)
     ax.set_xlim(0, 0.5*fs)
     ax.grid(True)
     ax.set_xlabel('Frequency (Hz)')
     ax.set_ylabel('Gain (dB)')
     ax.set_title(title)

def plot_stem(w,h,fs,title):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    r=0.5*fs*w/np.pi
    rr=20*np.log10(np.abs(h))
    gain=[]
    freq=[]
    for i in range(len(rr)):
       if rr[i]>=-12 and rr[i]<=12:
          gain.append(rr[i])
          freq.append(r[i])

    gain=np.array(gain)
    freq=np.array(freq)
    ax.stem(freq,gain)
    ax.set_ylim(-15,15)
    ax.set_xlim(0,0.5*fs)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Gain (dB)')
    ax.set_title(title)

def highpass_filter(fs,cutoff,trans_width,numtaps):
     taps=remez(numtaps,[0,cutoff-trans_width,cutoff,0.5*fs],[0,1],Hz=fs)
     w,h=freqz(taps,[1],worN=2000)
     return w,h




sample_rate=44100
taps=10
width=1
low=31.25
high=62.5
tps=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w,h=freqz(tps,worN=100)
plot_stem(w,h,sample_rate,"Band-pass Filter #1")



taps=10
width=10
low=62.5
high=125
tps2=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w2,h2=freqz(tps2,worN=100)
plot_stem(w2,h2,sample_rate,"Band-pass Filter #2")




taps=10
width=10
low=125
high=250
tps3=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w3,h3=freqz(tps3,worN=100)
plot_stem(w3,h3,sample_rate,"Band-pass Filter #3")



taps=10
width=10
low=250
high=500
tps4=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w4,h4=freqz(tps2,worN=100)
plot_stem(w4,h4,sample_rate,"Band-pass Filter #4")

taps=10
width=10
low=500
high=1000
tps5=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w5,h5=freqz(tps5,worN=100)
plot_stem(w5,h5,sample_rate,"Band-pass Filter #5")



taps=10
width=10
low=1000
high=2000
tps6=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w6,h6=freqz(tps6,worN=100)
plot_stem(w6,h6,sample_rate,"Band-pass Filter #6")



taps=10
width=10
low=2000
high=4000
tps7=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w7,h7=freqz(tps7,worN=100)
plot_stem(w7,h7,sample_rate,"Band-pass Filter #7")


taps=10
width=100
low=4000
high=8000
tps8=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w8,h8=freqz(tps8,worN=100)
plot_stem(w8,h8,sample_rate,"Band-pass Filter #8")

taps=10
width=200
low=8000
high=16000
tps9=bandpass_remez(ntaps=taps,lowcut=low,highcut=high,fs=sample_rate,width=width)
w9,h9=freqz(tps9,worN=100)
plot_stem(w9,h9,sample_rate,"Band-pass Filter #9")

vectorcoeficienctes=[tps,tps2,tps3,tps4,tps5,tps6,tps7,tps8,tps9]
t = np.linspace(0,1,1000, False)
sig=np.sin(2*np.pi*600*t)+np.sin(2*np.pi*1200*t)
def ecualizador(gain,x):
  listaajuste=[]
  contador=0
  for i in gain:
      listaajuste.append(20*np.log10(i)*i[contador])
      contador+=1
  arreglo=np.array(listaajuste)
  arreglo[np.isnan(arreglo)]=0
  y=lfilter(tps,1,x=arreglo)
  #print(np.sum(arreglo))
  #print(arreglo)
  return y
eye=ecualizador(vectorcoeficienctes,sig)
