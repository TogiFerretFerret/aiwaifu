import pyaudio
interface = pyaudio.PyAudio()
class AudioLoop:
    def __init__(self, video_mode="camera"):
        self.vmode = video_mode
        self.queued_audio = None
        self.out_queue = None
        self.
