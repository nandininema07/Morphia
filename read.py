from pedalboard.io import AudioFile

# Open your audio file
with AudioFile('voice.wav') as f:
    audio = f.read(f.frames)
    print(f"Audio shape: {audio.shape}")
    print(f"Sample rate: {f.samplerate}")
