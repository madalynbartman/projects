import librosa
import numpy as np
import matplotlib.pyplot as plt
import requests

def download_song(url, filename='song.mp3'):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename

def visualize_audio(filename):
    # Load the audio file
    y, sr = librosa.load(filename, sr=None)

    # Create a figure with subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    # Plot the waveform
    axs[0].plot(y)
    axs[0].set_title('Waveform')
    axs[0].set_xlabel('Samples')
    axs[0].set_ylabel('Amplitude')

    # Plot the spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=axs[1], cmap='coolwarm')
    axs[1].set_title('Spectrogram')
    fig.colorbar(img, ax=axs[1], format='%+2.0f dB')

    plt.tight_layout()
    plt.show()

# Example Usage
# Download the song (you can replace this URL with a direct audio file URL)
# url = 'YOUR_SPOTIFY_AUDIO_FILE_URL'
# filename = download_song(url)
# visualize_audio(filename)

# Before running, make sure you have the required libraries installed 
# pip install librosa matplotlib numpy requests

# For testing, you can replace 'filename' with a local audio file path
visualize_audio('path_to_your_local_audio_file.mp3')
