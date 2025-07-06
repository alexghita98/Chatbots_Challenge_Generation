import wave
import numpy as np

# Open the WAV file
with wave.open("secret.wav", "rb") as f:
    n_frames = f.getnframes()
    raw = f.readframes(n_frames)

# Convert byte data to 16-bit signed integers
samples = np.frombuffer(raw, dtype=np.int16)

# Extract LSBs from the first N samples
num_bits = 8 * 27  # Length of "flag{audio_stego_detected}"
bits = [(sample & 1) for sample in samples[:num_bits]]

# Reconstruct characters from bits
chars = [chr(int(''.join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8)]
message = ''.join(chars)

print(message)
