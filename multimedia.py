import numpy as np
import librosa
import soundfile as sf
import noisereduce as nr

# 1️⃣ Load Audio
file_path = r"C:\Users\nidhi\Desktop\yolo\pragati.mp3"
audio, fs = librosa.load(file_path, sr=None)

print("Audio Loaded Successfully")
print("Sampling Rate:", fs)

# 2️⃣ Noise Reduction (Strong but clean)
audio = nr.reduce_noise(y=audio, sr=fs, prop_decrease=1.0)

# 3️⃣ STFT (Frequency Domain Processing)
stft = librosa.stft(audio)
magnitude, phase = librosa.magphase(stft)

# 4️⃣ Enhance Speech Frequencies (300Hz – 3400Hz)
freqs = librosa.fft_frequencies(sr=fs)
mask = (freqs >= 300) & (freqs <= 3400)

# Apply mask to enhance speech band
enhanced_magnitude = magnitude.copy()
enhanced_magnitude[~mask, :] *= 0.2   # Reduce unwanted frequencies
enhanced_magnitude[mask, :] *= 1.5    # Boost speech frequencies

# 5️⃣ Reconstruct Signal
enhanced_stft = enhanced_magnitude * phase
enhanced_audio = librosa.istft(enhanced_stft)

# 6️⃣ Normalize Output
enhanced_audio = enhanced_audio / np.max(np.abs(enhanced_audio))

# 7️⃣ Save File
sf.write("enhanced_speech_output.wav", enhanced_audio, fs)

print("Enhanced high-quality speech saved successfully!")
