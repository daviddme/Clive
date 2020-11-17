import speech_recognition as voice
import playsound
from gtts import gTTS
import requests
import json
import os
import webbrowser

def bot_speak(voice_data):

    if "how are you" in voice_data.lower():
        audio_string = "I'm great and you?"
    elif "how old are you" in voice_data.lower():
        audio_string = "I never give my age."
    elif 'bitcoin' in voice_data.lower():
        r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        a = json.loads(r.text)
        audio_string = "1 bitcoin will cost you " + str(a["bitcoin"]["usd"]) + " US dollars."
    elif 'launch youtube' in voice_data.lower():
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)
        audio_string = "Opening YouTube"
    elif 'search youtube' in voice_data.lower():
        keyword = voice_data.split("for")[-1]

        url = f"https://www.youtube.com/results?search_query={keyword}"
        webbrowser.get().open(url)
        audio_string = "Search YouTube for " + str(keyword)
    else:
        audio_string = "I'd didn't get that sorry."
    
    tts = gTTS(text=audio_string, lang="en")
    audio_file = 'audio.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    #os.remove(audio_file)

#bot_speak()

rec = voice.Recognizer()

def bot_listen():

    with voice.Microphone(device_index=2) as source:
       audio = rec.listen(source)
       voice_data = ""
       try :
           voice_data = rec.recognize_google(audio)
       except e:
            print("I didn't get that")
    print(f"You Said : {voice_data}")
    bot_speak(voice_data)

bot = bot_listen()

