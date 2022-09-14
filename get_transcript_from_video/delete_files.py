import os


def delete_content():
    print('Files are about to be deleted.')
    files = ['video_files.txt', 'audio_files.txt', 'wav_files.txt']

    with open(files[0]) as f:
        video_data = f.readlines()
    video_files_path = [f"video_files/{item}".strip('\n') for item in video_data]    

    with open(files[1]) as f:
        audio_data = f.readlines()
    audio_files_path = [f"audio_files/{item}".strip('\n') for item in audio_data]    

    with open(files[2]) as f:
        wav_data = f.readlines()
    wav_files_path = [f"wav_files/{item}".strip('\n') for item in wav_data]   

    trash_list = video_files_path + audio_files_path + wav_files_path + files

    print(trash_list)  

    for file in trash_list:
        os.remove(file)



delete_content()        