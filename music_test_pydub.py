import pyaudio 
import wave
import numpy

sound1 = wave.open("resources/music/thunder-theme.wav", 'rb')
sound2 = wave.open("resources/music/thunder-theme.wav", 'rb')

def callback(frame_count):
    data1 = sound1.readframes(frame_count)
    data2 = sound2.readframes(frame_count)
    decodeddata1 = numpy.fromstring(data1, numpy.int16)
    decodeddata2 = numpy.fromstring(data2, numpy.int16)
    newdata = (decodeddata1 * 0.5 + decodeddata2* 0.5).astype(numpy.int16)
    return (newdata.tostring(), pyaudio.paContinue)

callback(128)