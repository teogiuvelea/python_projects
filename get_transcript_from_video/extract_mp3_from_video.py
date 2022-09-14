from moviepy.editor import *


def get_audio():
    with open('video_files.txt') as f:
        files = f.readlines()

    for file in files:
            
        video_file_name = file.strip('\n')
        video = VideoFileClip(f"video_files/{video_file_name}")
        audio = video.audio
        audio_file_name = f"audio_{video_file_name.split('.')[0]}.mp3"
        audio.write_audiofile(f"audio_files/{audio_file_name}")
    print('Get audio function has been completed.')    