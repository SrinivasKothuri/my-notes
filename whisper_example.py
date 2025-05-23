# Create a venv and follow the steps described at https://github.com/openai/whisper to install whisper and its dependencies
import sounddevice as sd
from scipy.io.wavfile import write
import datetime
import whisper

def record_audio(duration=5, filename="command.wav"):
    print(f"Recording for {duration} seconds...")
    fs = 44100  # Sample rate
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write(filename, fs, recording)
    print("Recording saved to", filename)
    return filename

model = whisper.load_model("base")  # Or 'small', 'medium', 'large'

def transcribe_audio(file_path):
    print("Transcribing audio...")
    result = model.transcribe(file_path)
    text = result["text"]
    return text

if __name__ == "__main__":
    audio_file = record_audio(duration=15)
    text = transcribe_audio(audio_file)
    print("Transcribed text:", text)
