import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def phase_encode(message, audio_file, output_file):
    # Read original audio
    rate, data = wavfile.read(audio_file)
    
    # Convert message to binary
    binary_msg = ''.join(format(ord(c), '08b') for c in message)
    binary_msg += '00000000'  # Null terminator
    
    # Perform FFT
    fft_data = np.fft.fft(data)
    phases = np.angle(fft_data)
    
    # Encode in phase components
    msg_index = 0
    for i in range(1, len(phases)):  # Skip DC component
        if msg_index < len(binary_msg):
            if binary_msg[msg_index] == '1':
                phases[i] += np.pi/2  # Encode 1
            else:
                phases[i] -= np.pi/2  # Encode 0
            msg_index += 1
    
    # Reconstruct signal
    modified_fft = np.abs(fft_data) * np.exp(1j * phases)
    modified_data = np.fft.ifft(modified_fft).real.astype(np.int16)
    
    # Save new audio
    wavfile.write(output_file, rate, modified_data)

# Usage
message = "FLAG{ph4se_3nc0d1ng}"
phase_encode(message, "clean_audio.wav", "secret_audio.wav")