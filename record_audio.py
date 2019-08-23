#Recording audio with sounddevice
import sounddevice as sd
from scipy.io.wavfile import write
#set sample rate
fs = 44100
#set recording duration
seconds = 3

myaudio = sd.rec(int(seconds*fs), samplerate = fs, channels = 2)
sd.wait() 
#name the output file

#now save myaudio as .wav file
write('firstaudio.wav',fs, myaudio)
