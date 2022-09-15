import speech_recognition as sr
from pydub import AudioSegment


def transcript():
# convert mp3 file to wav  
        with open('audio_files.txt') as f:
                audio_files = f.readlines()

        for file in audio_files:
                print(file.strip('\n'))  
                src = file.strip('\n')

                if "en" in src:
                    lang = 'en-US'
                elif "ro" in src:
                    lang = 'ro-RO'
                elif "sp" in src:
                    lang = 'sp-MX'    

                # source = "audio_test.mp3"
                sound = AudioSegment.from_mp3(f"audio_files/{src}")
                wav_format = f"{src.split('.')[0]}.wav"
                sound.export(f"wav_files/{wav_format}", format="wav")

                file_audio = sr.AudioFile(f"wav_files/{wav_format}")

                print('Mp3 file has been converted into a .wav file')
                # use the audio file as the audio source                                        
                r = sr.Recognizer()
                with file_audio as source:
                        r.adjust_for_ambient_noise(source)
                        audio_text = r.record(source)

                # print(type(audio_text))
                
                text = r.recognize_google(audio_text, language=lang)
                with open(f"transcripts/{src.split('.')[0]}.txt", 'w', encoding="utf-8") as f:
                        f.write(text)
                        
                print(text)
                print('.wav file has been transcribed and saved in a .txt file.')
                # with file_audio as source:
                #         print("Start transcribing file...")
                #         r.adjust_for_ambient_noise(source)
                #         audio = r.record(source)
                #         print(r.recognize_google(audio, language="en-US"))
                        
# transcript()                        