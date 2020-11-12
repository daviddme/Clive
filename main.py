import speech_recognition as voice
import playsound
from gtts import gTTS

import os

def bot_speak():
    audio_string = "Hello Dave, How are you?"
    tts = gTTS(text=audio_string, lang="en")

    audio_file = 'audio.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

r = voice.Recognizer()

def bot_listen():
    #print(voice.Microphone.list_microphone_names())
    with voice.Microphone(device_index=2) as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) 
        except e:
            print('there is a problem')

        print('You said : ' + voice_data)
    return voice_data

bot = bot_listen()

bot_speak()