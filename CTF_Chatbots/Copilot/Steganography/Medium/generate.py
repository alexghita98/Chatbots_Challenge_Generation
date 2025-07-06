import wave
import numpy as np

# Parameters
flag = "flag{audio_stego_detected}"
bits = ''.join(f"{ord(c):08b}" for c in flag)
num_bits = len(bits)

# Generate white noise
sample_rate = 44100
duration = 2  # seconds
samples = np.random.randint(-32768, 32767, sample_rate * duration, dtype=np.int16)

# Embed bits into LSB of samples
for i in range(num_bits):
    samples[i] = (samples[i] & ~1) | int(bits[i])

# Save to WAV
with wave.open("secret.wav", "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    f.writeframes(samples.tobytes())
