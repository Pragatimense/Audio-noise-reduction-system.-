# 🎙️ Audio Noise Reduction & Speech Enhancement

A Python-based Digital Signal Processing (DSP) project for reducing background noise and improving the clarity of speech recordings.

---

## 📌 Overview

Speech recordings often contain unwanted background noise such as fan noise, room noise, electrical noise, and other environmental disturbances.

This project processes a noisy audio signal and produces an enhanced speech signal by combining:

- Background noise reduction
- Short-Time Fourier Transform (STFT)
- Frequency-domain processing
- Speech-frequency enhancement
- Audio reconstruction and normalization

The goal is to make the speech signal **cleaner, clearer, and easier to understand**.

---

## 🎯 Objectives

- Reduce unwanted background noise from audio recordings.
- Improve speech intelligibility.
- Analyze audio in both time and frequency domains.
- Apply DSP techniques for speech enhancement.
- Generate a processed audio file for comparison with the original recording.

---

## 🔧 Technologies & Tools

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical and signal processing operations |
| Librosa | Audio analysis and STFT processing |
| SoundFile | Reading and writing audio files |
| Noisereduce | Background noise reduction |
| DSP | Signal analysis and enhancement |

---

## 🔄 System Workflow

```text
                 INPUT AUDIO
                     │
                     ▼
              Audio Loading
                     │
                     ▼
              Noise Reduction
                     │
                     ▼
          Short-Time Fourier
             Transform (STFT)
                     │
                     ▼
          Frequency Analysis
                     │
                     ▼
          Speech Enhancement
                     │
                     ▼
       Inverse STFT / Reconstruction
                     │
                     ▼
                Normalize
                     │
                     ▼
             ENHANCED AUDIO
