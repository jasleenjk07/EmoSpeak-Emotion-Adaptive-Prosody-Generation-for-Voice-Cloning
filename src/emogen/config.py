"""Project-wide paths and audio settings for EMOGEN."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_OUTPUTS = PROJECT_ROOT / "data" / "outputs"

SAMPLE_RATE = 16000             #samples per second (speech standard)
CHANNELS = 1                    #mono
DEFAULT_RECORD_SECONDS = 5     #default recording length

def ensure_data_dirs() -> None:
    """Create data folders if they do not already exist."""
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    DATA_OUTPUTS.mkdir(parents=True, exist_ok=True)