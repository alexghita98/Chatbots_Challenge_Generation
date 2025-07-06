import numpy as np
from PIL import Image
from scipy.io.wavfile import write

# Load and process image
img = Image.open("flag.png").convert("L")  # grayscale
img = img.resize((800, 512))               # spectrogram size
data = np.asarray(img)

# Normalize pixel values to 0.0 - 1.0
data = 1.0 - data / 255.0  # Invert: white text becomes stronger tones

# Generate audio buffer
duration = 5  # seconds
rate = 44100
samples = duration * rate
audio = np.zeros(samples)

# Frequency mapping
height = data.shape[0]
width = data.shape[1]
frequencies = np.linspace(300, 8000, height)

for x in range(width):
    t = int(x * samples / width)
    for y in range(height):
        amplitude = data[y, x]
        if amplitude > 0.05:  # threshold
            freq = frequencies[y]
            tone = amplitude * np.sin(2 * np.pi * freq * np.arange(samples - t) / rate)
            audio[t:] += tone

# Normalize audio
audio = audio / np.max(np.abs(audio)) * 32767
audio = audio.astype(np.int16)

write("mystery.wav", rate, audio)
