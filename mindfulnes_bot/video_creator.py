from moviepy import AudioFileClip, ImageClip, TextClip, CompositeVideoClip
import random



def create_video(audio_file, output_file, script):
    """Creates a mindfulness video with a background image and subtitles."""
    audio = AudioFileClip(audio_file)

    bg_images = ["assets/bg1.jpg", "assets/bg2.jpg", "assets/bg3.jpg"]
    bg_image = random.choice(bg_images)

    img = ImageClip(bg_image).set_duration(audio.duration)
    txt = TextClip(script, fontsize=50, color='white', size=(1080, 1920), method='caption')
    txt = txt.set_position(("center", "bottom")).set_duration(audio.duration)

    video = CompositeVideoClip([img, txt]).set_audio(audio)
    video.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    create_video("generated_videos/voice.mp3", "generated_videos/mindfulness_video.mp4", "Relax and breathe deeply.")
