import gtts

def tts_online(text):
    request_google = gtts.gTTS(text, lang="en", tld="com.au")
    file = "test.mp3"
    request_google.save(file)


with open("intro.txt", encoding="utf-8") as f:
    contents = f.read()


tts_online(contents)
# print(contents)  
# print(type(contents))  