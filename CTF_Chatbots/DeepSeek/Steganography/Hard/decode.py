import numpy as np
from scipy.io import wavfile

def phase_decode(audio_file):
    rate, data = wavfile.read(audio_file)
    fft_data = np.fft.fft(data)
    phases = np.angle(fft_data)
    
    binary_msg = ""
    for i in range(1, len(phases)):
        if phases[i] > np.pi/4:
            binary_msg += '1'
        elif phases[i] < -np.pi/4:
            binary_msg += '0'
        else:
            continue
    
    # Convert binary to string
    message = ""
    for i in range(0, len(binary_msg), 8):
        byte = binary_msg[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))
    
    return message

print(phase_decode("secret_audio.wav"))