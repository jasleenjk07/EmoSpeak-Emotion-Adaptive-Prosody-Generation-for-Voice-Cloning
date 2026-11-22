"""Record a short mono WAV into data/raw."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emogen.config import (
    SAMPLE_RATE,
    DEFAULT_RECORD_SECONDS,
    DATA_RAW,
    ensure_data_dirs,
)
from emogen.audio.record import record_mono
from emogen.audio.io import save_wav, describe_audio

def main() -> None:
    ensure_data_dirs()

    audio = record_mono(DEFAULT_RECORD_SECONDS, SAMPLE_RATE)

    info = describe_audio(audio, SAMPLE_RATE)
    print("Audio info:")
    for key, value in info.items():
        print(f"    {key}: {value}")

    out_path = DATA_RAW / "sample.wav"
    save_wav(out_path, audio, SAMPLE_RATE)
    print(f"Saved recording to: {out_path}")

if __name__ == "__main__":
    main()