from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from gtts import gTTS
from pygame import mixer
from time import sleep


class AudioPlayer:

    def __init__(
        self,
        volume: float = 1.0,
        language: str = "it",  # TODO: support multiple languages
    ) -> None:
        mixer.init()
        self.player = mixer.music
        self.player.set_volume(volume)
        self.language = language

    def audio_create(self, text: str, audio_file: str):
        """Creates audio file"""
        audio = gTTS(text=text, lang=self.language, slow=False)
        audio.save(audio_file)

    def audio_start(self, audio_file):
        self.player.load(audio_file)
        self.player.play()
        while self.player.get_busy() == True:
            sleep(1)
