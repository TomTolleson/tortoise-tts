import torch
import torchaudio
import utils.audio
import tortoise.api as api

# Load your voice samples
clips_paths = ['voices/tom/sample1.wav', 'voices/tom/sample2.wav']
reference_clips = [utils.audio.load_audio(p, 22050) for p in clips_paths]

# Initialize TTS
tts = api.TextToSpeech()

# Generate speech
text = "This is a test of my cloned voice"
pcm_audio = tts.tts_with_preset(text, voice_samples=reference_clips, preset='fast')