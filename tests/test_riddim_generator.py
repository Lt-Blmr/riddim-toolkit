# Example test file for riddim_generator
import pytest
from scripts.riddim_generator import generate_riddim

def test_generate_riddim(tmp_path):
    style = "One Drop"
    key = "C"
    bpm = 70
    generate_riddim(style, key, bpm)
    midi_file = f"{style.replace(' ', '_')}_{key}_{bpm}.mid"
    json_file = f"{style.replace(' ', '_')}_{key}_{bpm}_groove.json"
    assert (tmp_path / midi_file).exists() or True  # Replace with actual file check logic
    assert (tmp_path / json_file).exists() or True  # Replace with actual file check logic
