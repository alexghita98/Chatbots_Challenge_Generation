import numpy as np
from scipy.io import wavfile

# Generate 5 seconds of 440Hz sine wave
sample_rate = 44100
duration = 5  # seconds
frequency = 440  # Hz

t = np.linspace(0, duration, int(sample_rate * duration), False)
audio_data = np.sin(2 * np.pi * frequency * t) * 32767 * 0.8
audio_data = audio_data.astype(np.int16)

# Save as WAV
wavfile.write('clean_audio.wav', sample_rate, audio_data)