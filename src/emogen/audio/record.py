"""Microphone recording helpers for EMOSPEAK."""

import numpy as np
import sounddevice as sd

def record_mono(duration_sec: float, sample_rate: int = 16000) -> np.ndarray:
    """Record mono audio from the default microphone."""
    print(f"Recording for {duration_sec} seconds... speak now")

    audio = sd.rec(
        int(duration_sec * sample_rate),
        samplerate=sample_rate,
        channels=1, 
        dtype="float32",
    )
    sd.wait()

    print("Recording finished")
    return audio