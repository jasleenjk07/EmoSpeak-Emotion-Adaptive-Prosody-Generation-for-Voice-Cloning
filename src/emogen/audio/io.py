"""Load, save, and inspect WAV audio for EMOGEN."""

from pathlib import Path
import numpy as np
import soundfile as sf

def save_wav(path: Path | str, audio: np.ndarray, sample_rate: int) -> Path:
    """Save a NumPy audio array to a WAV file."""
    path = Path(path)
    sf.write(path, audio, sample_rate)
    return path

def load_wav(path: Path| str) -> tuple[np.ndarray, int]:
    """Load a WAV file and return (audio, sample_rate)."""
    path = Path(path)
    audio, sample_rate = sf.read(path, dtype="float32")
    return audio, sample_rate

def describe_audio(audio: np.ndarray, sample_rate: int) -> dict:
    """Return basic facts about an audio array."""
    num_samples = audio.shape[0]
    duration_sec = num_samples / sample_rate
    peak = float(np.max(np.abs(audio)))

    return {
        "shape": tuple(audio.shape),
        "num_samples": int(num_samples),
        "sample_rate": int(sample_rate),
        "duration_sec": float(duration_sec),
        "peak": peak
    }