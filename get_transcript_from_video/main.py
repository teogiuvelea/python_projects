from get_directory_items_title import directory_items
from extract_mp3_from_video import get_audio
from write_transcript import transcript



if __name__ == "__main__":

    directory_items('video_files')
    get_audio()
    directory_items('audio_files')
    transcript()
    directory_items('wav_files')
