# shitty definitions for shitty code 
# async's gonna be a NIGHTMARE
# object oriented (orbital strike cannon)
class Config:
    def __init__(self):
        self.voice_name="Leda"
        self.api_key=""
        with open("token.txt", "r") as f:
            self.api_key = f.read().strip()
        self.model="gemini-2.5-flash-native-audio-preview-12-2025"
