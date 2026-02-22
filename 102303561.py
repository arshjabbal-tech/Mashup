import sys
import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def convert_to_audio():
    os.makedirs("audios", exist_ok=True)

    for file in os.listdir():
        if file.endswith((".mp4", ".webm")):
            video_path = file
            audio_path = "audios/" + file + ".mp3"

            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(audio_path)
            clip.close()

def cut_audio(duration):
    os.makedirs("trimmed", exist_ok=True)

    for file in os.listdir("audios"):
        if file.endswith(".mp3"):
            audio = AudioSegment.from_mp3("audios/" + file)
            trimmed = audio[:duration * 1000]
            trimmed.export("trimmed/" + file, format="mp3")

def merge_audio(output_file):
    combined = AudioSegment.empty()

    for file in os.listdir("trimmed"):
        if file.endswith(".mp3"):
            combined += AudioSegment.from_mp3("trimmed/" + file)

    combined.export(output_file, format="mp3")

def main():
    if len(sys.argv) != 5:
        print("Usage: python program.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit()

    duration = int(sys.argv[3])
    output_file = sys.argv[4]

    convert_to_audio()
    cut_audio(duration)
    merge_audio(output_file)

    print("Mashup created successfully!")

if __name__ == "__main__":
    main()