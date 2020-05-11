import numpy as np
import math
import wave
import struct

"""
Turn a wave file into an array of ints
Wav file should not contain Metadata
"""
def get_samples(file):
     
    waveFile = wave.open(file, 'r')
    samples = []
 
    # Gets total number of frames
    length = waveFile.getnframes()
     
    # Read them into the frames array
    for i in range(0,length):
        waveData = waveFile.readframes(1)
        data = struct.unpack("%iB"%2, waveData)
         
        # After unpacking, each data array here is actually an array of ints
        # The length of the array depends on the number of channels you have
         
        # Drop to mono channel
        samples.append(int(data[0]))

    samples = np.array(samples)
    return samples

samples = get_samples("audio.wav")

print samples

def dct(samples):

    new_samples = samples
    samples_n = len(samples)

    for k in range(samples_n):
        e = 0

        for n in range(0, 8):
            e += samples[n] * math.cos((2 * math.pi * n * k)/(2 * 8) + (k * math.pi)/(2 * 8))

        if k == 0:
            c = math.sqrt(1/2)
        else:
            c = 1

        new_samples[k] = math.sqrt(2/8) * c * e

    return new_samples

new_samples = dct(samples)

print new_samples
