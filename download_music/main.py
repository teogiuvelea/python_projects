from pytube import YouTube
import os
from youtubesearchpython import VideosSearch

    
# searches youtube for a song's link address based on title song/artist
def search_for_songs(song_names):
    '''
    Takes a list of strings/song title/artist as input.
    Loops through the list and for each song/query returns just one result based on given limit
    The output of the query is a dictionary.
    From dictionary we access the key 'link' which contains the youtube url.
    URL gets appended to a list.
    The resulted list is then used to as input in another function.access and convert the video into a mp3 file in a. 
    '''
    links = []
    for name in song_names:
        title = name + 'lyrics'
        video_search = VideosSearch(title, limit=1)
        song = video_search.result()
        link = song['result'][0]['link']
        links.append(link)
        print(name, link)
    return links


# converts list of links to mp3 format songs 
def download_mp3(songs):
    '''
    Takes a list of youtube links, iterates through whole list, converts video to mp3.
    Saves file in a specific directory'''
    for song in songs:
        yt = YouTube(song)
        video = yt.streams.filter(only_audio=True).first()
        destination = "songs/"
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")

        
# reads data from songs.txt file
with open("songs.txt") as f:
    song_names = f.readlines()

# runs the functions with data read from file
if __name__ == "__main__":
    songs = search_for_songs(song_names)
    download_mp3(songs)
