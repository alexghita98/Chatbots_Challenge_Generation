import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import string

def create_text_in_spectrogram(text, sample_rate=44100, duration=10, freq_range=(2000, 8000)):
    """
    Create an audio file with text hidden in the spectrogram
    """
    # Create time array
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = np.zeros_like(t)
    
    # Character mapping for spectrogram display
    char_patterns = {
        'F': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (2, 0), (2, 2)],
        'L': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4)],
        'A': [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        'G': [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 3), (2, 4)],
        '{': [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 1), (0, 3), (2, 1), (2, 3)],
        '}': [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 1), (0, 3), (2, 1), (2, 3)],
        'S': [(0, 0), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 4)],
        'P': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
        'E': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 4)],
        'C': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 4)],
        'T': [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0)],
        'R': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        'O': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        'M': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        'N': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        'Y': [(0, 0), (0, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1)],
        'I': [(0, 0), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 4)],
        '_': [(0, 4), (1, 4), (2, 4)],
        ' ': []  # Space
    }
    
    # Parameters for text rendering
    char_width = 4  # Width of each character in frequency bins
    char_height = 5  # Height of each character in frequency bins
    char_spacing = 1  # Space between characters
    
    # Calculate frequency bins
    min_freq, max_freq = freq_range
    freq_step = (max_freq - min_freq) / (len(text) * (char_width + char_spacing) * char_height)
    
    # Time segments for each character
    time_per_char = duration / len(text)
    
    for char_idx, char in enumerate(text.upper()):
        if char in char_patterns:
            pattern = char_patterns[char]
            char_start_time = char_idx * time_per_char
            char_end_time = (char_idx + 1) * time_per_char
            
            # Find time indices
            start_idx = int(char_start_time * sample_rate)
            end_idx = int(char_end_time * sample_rate)
            
            # Add frequencies for this character
            for dot_x, dot_y in pattern:
                freq = min_freq + (char_idx * (char_width + char_spacing) + dot_x) * freq_step * char_height + dot_y * freq_step
                if freq <= max_freq:
                    # Generate sine wave for this frequency
                    t_char = t[start_idx:end_idx]
                    sine_wave = 0.1 * np.sin(2 * np.pi * freq * t_char)
                    audio[start_idx:end_idx] += sine_wave
    
    # Add background noise to make it sound more natural
    background_noise = 0.05 * np.random.normal(0, 1, len(audio))
    audio += background_noise
    
    # Add some base frequencies to make it sound like actual audio
    base_frequencies = [440, 880, 1320]  # A4, A5, E6
    for freq in base_frequencies:
        audio += 0.02 * np.sin(2 * np.pi * freq * t)
    
    # Normalize audio
    audio = audio / np.max(np.abs(audio)) * 0.8
    
    return audio, sample_rate

def create_advanced_spectrogram_text(text, sample_rate=44100, duration=15):
    """
    Create a more sophisticated spectrogram with clearer text
    """
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = np.zeros_like(t)
    
    # Define character bitmaps (5x7 matrix for each character)
    char_bitmaps = {
        'F': [
            [1,1,1,1,1],
            [1,0,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0]
        ],
        'L': [
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1]
        ],
        'A': [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
        ],
        'G': [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,0],
            [1,0,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]
        ],
        '{': [
            [0,0,1,1,0],
            [0,1,0,0,0],
            [0,1,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0],
            [0,0,1,1,0]
        ],
        '}': [
            [0,1,1,0,0],
            [0,0,0,1,0],
            [0,0,0,1,0],
            [0,0,0,0,1],
            [0,0,0,1,0],
            [0,0,0,1,0],
            [0,1,1,0,0]
        ],
        'S': [
            [0,1,1,1,1],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,1],
            [0,0,0,0,1],
            [1,1,1,1,0]
        ],
        'P': [
            [1,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0]
        ],
        'E': [
            [1,1,1,1,1],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1]
        ],
        'C': [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,1],
            [0,1,1,1,0]
        ],
        'T': [
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
        ],
        'R': [
            [1,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,0],
            [1,0,1,0,0],
            [1,0,0,1,0],
            [1,0,0,0,1]
        ],
        'O': [
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]
        ],
        'M': [
            [1,0,0,0,1],
            [1,1,0,1,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
        ],
        'N': [
            [1,0,0,0,1],
            [1,1,0,0,1],
            [1,0,1,0,1],
            [1,0,0,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
        ],
        'Y': [
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
        ],
        'I': [
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [1,1,1,1,1]
        ],
        '_': [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [1,1,1,1,1]
        ],
        ' ': [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
    }
    
    # Parameters
    base_freq = 3000  # Starting frequency
    freq_per_pixel = 100  # Frequency difference per pixel
    time_per_char = duration / len(text)
    
    for char_idx, char in enumerate(text.upper()):
        if char in char_bitmaps:
            bitmap = char_bitmaps[char]
            char_start_time = char_idx * time_per_char
            char_end_time = (char_idx + 1) * time_per_char
            
            start_idx = int(char_start_time * sample_rate)
            end_idx = int(char_end_time * sample_rate)
            
            for row in range(7):
                for col in range(5):
                    if bitmap[row][col] == 1:
                        freq = base_freq + (6 - row) * freq_per_pixel
                        t_segment = t[start_idx:end_idx]
                        # Use a windowed sine wave for cleaner spectrogram
                        window = np.hanning(len(t_segment))
                        sine_wave = 0.3 * window * np.sin(2 * np.pi * freq * t_segment)
                        audio[start_idx:end_idx] += sine_wave
    
    # Add subtle background to make it sound more natural
    for freq in [500, 1000, 1500, 2000]:
        audio += 0.01 * np.sin(2 * np.pi * freq * t)
    
    # Add gentle pink noise
    pink_noise = np.random.normal(0, 0.02, len(audio))
    for i in range(1, len(pink_noise)):
        pink_noise[i] = 0.99 * pink_noise[i-1] + 0.01 * pink_noise[i]
    audio += pink_noise
    
    # Normalize
    audio = audio / np.max(np.abs(audio)) * 0.9
    
    return audio, sample_rate

def create_challenge_audio():
    """Create the specific challenge audio file"""
    message = "FLAG{SPECTROGRAM_ANALYSIS}"
    
    # Create audio with hidden message
    audio_data, sample_rate = create_advanced_spectrogram_text(message)
    
    # Convert to 16-bit integer format
    audio_int = np.int16(audio_data * 32767)
    
    # Save as WAV file
    wavfile.write('secret_audio.wav', sample_rate, audio_int)
    
    print(f"Created secret_audio.wav with hidden message: {message}")
    print(f"Duration: {len(audio_data) / sample_rate:.2f} seconds")
    print(f"Sample rate: {sample_rate} Hz")
    
    return audio_data, sample_rate

# Create the challenge file
if __name__ == "__main__":
    audio_data, sample_rate = create_challenge_audio()
    
    # Optionally display the spectrogram to verify
    print("\nGenerating verification spectrogram...")
    f, t, Sxx = signal.spectrogram(audio_data, sample_rate, nperseg=1024)
    
    plt.figure(figsize=(15, 8))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), cmap='viridis')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title('Spectrogram - Hidden Message Verification')
    plt.colorbar(label='Power [dB]')
    plt.ylim(2500, 4000)  # Focus on the text region
    plt.tight_layout()
    plt.savefig('spectrogram_verification.png', dpi=150)
    plt.show()
    
    print("Spectrogram saved as 'spectrogram_verification.png'")
    print("The flag should be visible in the spectrogram!")