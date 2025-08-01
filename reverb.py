from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile

# Make an effect chain
board = Pedalboard([Reverb(room_size=0.2)])  # Adjust room size as needed

# Open input file
with AudioFile('voice.wav') as f:
    audio = f.read(f.frames)
    sample_rate = f.samplerate

# Apply effect
processed = board(audio, sample_rate)

# Save output
with AudioFile('voice_reverb.wav', 'w', sample_rate, audio.shape[0]) as f:
    f.write(processed)

print("Done! Check voice_reverb.wav")
