import moviepy.editor


def main():
    video = moviepy.editor.VideoFileClip("SilvernEMINEM -Silvername берёт карту берёт карту продаёт карту (RAP GOD COVER).mp4")
    audio = video.audio
    audio.write_audiofile("SilvernameEminem.mp3")


if __name__ == '__main__':
    main()
