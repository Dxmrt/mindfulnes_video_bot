from gtts import gTTS

def text_to_speech(text, filename="generated_videos/voice.mp3"):
    """Converts text into speech using gTTS."""
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    return filename

if __name__ == "__main__":
    text_to_speech("This is a test mindfulness message.")
