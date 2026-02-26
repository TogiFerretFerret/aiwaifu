import pyaudio
interface = pyaudio.PyAudio()
class AudioLoop:
    def __init__(self, video_mode="camera", session):
        self.vmode = video_mode
        self.queued_audio = None
        self.out_queue = None
        self.session = session 
        self.send_text_task = None
        self.receive_audio_task = None
        self.play_audio_task = None
        self.audio_stream = None
    async def send_text(self, text):
        if self.session is not None:
            await self.session.send(input=text or ".", end_of_turn=True)
