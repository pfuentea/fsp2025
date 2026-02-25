from gtts import gTTS
from pathlib import Path

texto="Sigue estas instrucciones antes de comenzar, gracias!"
tts=gTTS(texto,lang="es")

out=Path("./mensajes/intro_app/static/audio/intro.mp3")
out.parent.mkdir(parents=True, exist_ok=True)
tts.save(str(out))