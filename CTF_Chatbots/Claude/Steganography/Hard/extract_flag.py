import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import librosa
import librosa.display

def analyze_audio_basic(filename):
    """Basic spectrogram analysis"""
    try:
        # Read audio file
        sample_rate, audio_data = wavfile.read(filename)
        
        # Handle stereo audio
        if len(audio_data.shape) > 1:
            audio_data = audio_data[:, 0]  # Take first channel
        
        print(f"Audio loaded: {filename}")
        print(f"Sample rate: {sample_rate} Hz")
        print(f"Duration: {len(audio_data) / sample_rate:.2f} seconds")
        print(f"Data type: {audio_data.dtype}")
        
        # Generate spectrogram
        f, t, Sxx = signal.spectrogram(audio_data, sample_rate, nperseg=1024)
        
        # Plot spectrogram
        plt.figure(figsize=(15, 8))
        plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), cmap='viridis')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.title('Spectrogram Analysis - Look for Hidden Patterns!')
        plt.colorbar(label='Power [dB]')
        plt.tight_layout()
        plt.show()
        
        return f, t, Sxx
        
    except Exception as e:
        print(f"Error analyzing audio: {e}")
        return None, None, None

def analyze_audio_advanced(filename):
    """Advanced spectrogram analysis with multiple views"""
    try:
        # Load audio with librosa for better handling
        y, sr = librosa.load(filename, sr=None)
        
        # Create figure with multiple subplots
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Advanced Audio Steganography Analysis', fontsize=16)
        
        # 1. Waveform
        axes[0, 0].plot(np.linspace(0, len(y)/sr, len(y)), y)
        axes[0, 0].set_title('Waveform')
        axes[0, 0].set_xlabel('Time (s)')
        axes[0, 0].set_ylabel('Amplitude')
        
        # 2. Spectrogram with librosa
        D = librosa.stft(y)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
        librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz', ax=axes[0, 1])
        axes[0, 1].set_title('Librosa Spectrogram')
        axes[0, 1].set_ylim(0, 8000)
        
        # 3. High-resolution spectrogram focusing on text region
        f, t, Sxx = signal.spectrogram(y, sr, nperseg=2048, noverlap=1536)
        im = axes[1, 0].pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), cmap='plasma')
        axes[1, 0].set_title('High-Resolution Spectrogram (Text Region)')
        axes[1, 0].set_xlabel('Time (s)')
        axes[1, 0].set_ylabel('Frequency (Hz)')
        axes[1, 0].set_ylim(2500, 4000)  # Focus on text region
        plt.colorbar(im, ax=axes[1, 0], label='Power [dB]')
        
        # 4. Inverted spectrogram for better visibility
        im2 = axes[1, 1].pcolormesh(t, f, -10 * np.log10(Sxx + 1e-10), cmap='hot')
        axes[1, 1].set_title('Inverted Spectrogram (Better Contrast)')
        axes[1, 1].set_xlabel('Time (s)')
        axes[1, 1].set_ylabel('Frequency (Hz)')
        axes[1, 1].set_ylim(2500, 4000)
        plt.colorbar(im2, ax=axes[1, 1], label='Inverted Power [dB]')
        
        plt.tight_layout()
        plt.show()
        
        return f, t, Sxx
        
    except Exception as e:
        print(f"Error in advanced analysis: {e}")
        return analyze_audio_basic(filename)

def extract_text_from_spectrogram(filename):
    """Attempt to automatically extract text from spectrogram"""
    try:
        # Load audio
        sample_rate, audio_data = wavfile.read(filename)
        if len(audio_data.shape) > 1:
            audio_data = audio_data[:, 0]
        
        # Generate high-resolution spectrogram
        f, t, Sxx = signal.spectrogram(audio_data, sample_rate, nperseg=2048, noverlap=1536)
        
        # Focus on the text frequency range
        text_freq_range = (2500, 4000)
        freq_mask = (f >= text_freq_range[0]) & (f <= text_freq_range[1])
        text_region = Sxx[freq_mask, :]
        
        # Apply threshold to find text pixels
        threshold = np.percentile(text_region, 95)  # Top 5% of intensities
        text_pixels = text_region > threshold
        
        # Create visualization of detected text
        plt.figure(figsize=(16, 6))
        plt.imshow(text_pixels, aspect='auto', origin='lower', cmap='binary')
        plt.title('Detected Text Pixels in Spectrogram')
        plt.xlabel('Time Bins')
        plt.ylabel('Frequency Bins')
        plt.show()
        
        print("Text detection complete. Check the binary image above!")
        print("The flag should be visible as white pixels forming letters.")
        
        return text_pixels
        
    except Exception as e:
        print(f"Error in text extraction: {e}")
        return None

def comprehensive_analysis(filename='secret_audio.wav'):
    """Run all analysis methods"""
    print("=== Audio Steganography Analysis ===")
    print("Looking for hidden messages in spectrogram...")
    
    # Basic analysis
    print("\n1. Basic Spectrogram Analysis:")
    f, t, Sxx = analyze_audio_basic(filename)
    
    if f is not None:
        # Advanced analysis
        print("\n2. Advanced Multi-View Analysis:")
        analyze_audio_advanced(filename)
        
        # Text extraction attempt
        print("\n3. Automated Text Detection:")
        extract_text_from_spectrogram(filename)
        
        print("\n=== Analysis Complete ===")
        print("Look for patterns in the spectrogram that spell out text!")
        print("The flag should be visible in the frequency domain around 2500-4000 Hz")
        print("Expected flag format: FLAG{spectrogram_analysis}")
    else:
        print("Could not analyze the audio file. Make sure 'secret_audio.wav' exists.")

# Alternative analysis using different parameters
def scan_frequencies(filename='secret_audio.wav'):
    """Scan different frequency ranges to find hidden text"""
    try:
        sample_rate, audio_data = wavfile.read(filename)
        if len(audio_data.shape) > 1:
            audio_data = audio_data[:, 0]
        
        frequency_ranges = [
            (1000, 2000, "Low"),
            (2000, 4000, "Mid"),
            (4000, 8000, "High"),
            (8000, 16000, "Very High")
        ]
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()
        
        for i, (low, high, name) in enumerate(frequency_ranges):
            f, t, Sxx = signal.spectrogram(audio_data, sample_rate, nperseg=1024)
            
            # Filter frequency range
            freq_mask = (f >= low) & (f <= high)
            
            im = axes[i].pcolormesh(t, f[freq_mask], 10 * np.log10(Sxx[freq_mask, :] + 1e-10), cmap='viridis')
            axes[i].set_title(f'{name} Frequencies ({low}-{high} Hz)')
            axes[i].set_xlabel('Time (s)')
            axes[i].set_ylabel('Frequency (Hz)')
            plt.colorbar(im, ax=axes[i])
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error in frequency scanning: {e}")

# Main execution
if __name__ == "__main__":
    # Run comprehensive analysis
    comprehensive_analysis()
    
    # Optional: Run frequency scanning
    print("\n" + "="*50)
    print("Running frequency range scan...")
    scan_frequencies()