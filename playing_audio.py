#Playing audio with python-sounddevice and soundfile
import soundfile as sf
import sounddevice as sd
file = 'C:/Users/UPES/Pictures/Audio_Speech_analysis/data/kaggle_audio_analysis/audio_test/00c4d5b8.wav'
data, fs = sf.read(file, dtype = 'float32')
sd.play(data, fs)
status = sd.wait() #wait until file is done playing
