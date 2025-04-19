import json
import os
from mido import Message, MidiFile, MidiTrack, bpm2tempo

def generate_riddim(style: str, key: str, bpm: int):
    print(f"Generating riddim: {style} | Key: {key} | BPM: {bpm}")
    
    # File names
    filename_base = f"{style.replace(' ', '_')}_{key}_{bpm}"
    midi_filename = f"{filename_base}.mid"
    json_filename = f"{filename_base}_groove.json"

    # Create a new MIDI file
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Set tempo
    tempo = bpm2tempo(bpm)
    track.append(Message('program_change', program=1, time=0))  # Set instrument
    track.append(Message('control_change', control=7, value=100, time=0))  # Volume
    track.append(Message('control_change', control=10, value=64, time=0))  # Pan

    # Example pattern: Kick on beat 1 & 3, snare on 2 & 4
    quarter_note = int(mid.ticks_per_beat)
    pattern = [
        ('kick', 36, 0),
        ('snare', 38, quarter_note),
        ('kick', 36, quarter_note),
        ('snare', 38, quarter_note),
    ]

    for i in range(4):  # 1 bar loop
        for name, note, delay in pattern:
            track.append(Message('note_on', note=note, velocity=90, time=delay if delay > 0 else 0))
            track.append(Message('note_off', note=note, velocity=0, time=int(quarter_note / 2)))

    mid.save(midi_filename)
    print(f"Saved MIDI: {midi_filename}")

    # Groove map as JSON
    groove_data = {
        "style": style,
        "key": key,
        "bpm": bpm,
        "pattern": [
            {"instrument": "kick", "beat": 1},
            {"instrument": "snare", "beat": 2},
            {"instrument": "kick", "beat": 3},
            {"instrument": "snare", "beat": 4}
        ]
    }

    with open(json_filename, 'w') as f:
        json.dump(groove_data, f, indent=2)
    print(f"Saved Groove JSON: {json_filename}")


if __name__ == '__main__':
    generate_riddim("One Drop", "C", 70)
