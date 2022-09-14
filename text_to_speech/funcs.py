import gtts
import pyttsx3


def tts_online(text, file_title):
    request_google = gtts.gTTS(text, lang="en", tld="co.uk")
    request_google.save(f"{file_title}.mp3")


def tts_offline(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 145)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    with open(text, encoding="utf-8") as f:
            contents = f.read()
    engine.say(contents)
    engine.runAndWait()


def tts_save_files(input_files):
    for file_name in input_files:
        with open(file_name, encoding="utf-8") as f:
            contents = f.read()
        tts_online(contents, file_name[:-4])  

  