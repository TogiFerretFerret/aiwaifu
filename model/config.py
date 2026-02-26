# shitty definitions for shitty code 
# async's gonna be a NIGHTMARE
# object oriented (orbital strike cannon)
from google.genai import types
from model.tools import tools
class Config:
    def __init__(self):
        self.voice_name="Leda"
        self.api_key=""
        with open("token.txt", "r") as f:
            self.api_key = f.read().strip()
        self.model="gemini-2.5-flash-native-audio-preview-12-2025"
        self.liveConfig = types.LiveConnectConfig(
            response_modalities=[types.Modality("AUDIO")],
            media_resolution=types.MediaResolution("MEDIA_RESOLUTION_MEDIUM"),
            speech_config=types.SpeechConfig(voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=self.voice_name)
            )),
            context_window_compression=types.ContextWindowCompressionConfig(
                trigger_tokens=104857,
                sliding_window=types.SlidingWindow(target_tokens=104857)
            ),
            tools=tools
        )
