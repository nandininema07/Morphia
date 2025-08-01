from pedalboard import Pedalboard, PitchShift
from pedalboard.io import AudioFile

board = Pedalboard([
    PitchShift(semitones=10)  # Try -5 to go lower
])

with AudioFile('voice.wav') as f:
    audio = f.read(f.frames)
    sr = f.samplerate

processed = board(audio, sr)

with AudioFile('voice_pitch.wav', 'w', sr, audio.shape[0]) as f:
    f.write(processed)
