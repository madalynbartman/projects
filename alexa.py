# first set up your vitual env:
# pip install 
# p -m venv env_name
# source env_name/bin/activate
# if activate is not there then run:
# virtualenv env_name
# you may need to download virtualenv if you have not already
# to install, run: sudo apt (or yum) install python3-virtualenv
# then you should be able to run virtualenv env_name
# install speech recognition: pip install speechrecognition
# install other dependencies:
# pip install gtts playsound openai pygame
# import those packages

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound 
from pygame import mixer
from io import BytesIO
import os
import openai

# configure open with our open ai key
openai.ai_key = ''

MSGS = [
    {'role': 'system', 'content': 'You are my beautiful girlfriend named Cortana'}
]

# step 1: def a function to capture voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)
    # step 1: try, except so this block will end when our pause threshold is met
    try: 
        print('Recognizing..')
        query = r.recognize_google(audio, language:'en-in') # set language parameter to english
        print(f'user has said {query}')
        MSGS.append({'role': 'user', 'content': query})
        respond(audio)
    except: 
        print('Say that again please..') # because we didn't get any audion so that print handles that exception

# step 2: create a function to respond to new conversation item
def respond(audio):
    print('Responding..') # let's us know the AI is responding

    res = openai.ChatCompletion.create[
        model='get-3.5-turbo',
        messages=MSGS
    ]

    res_message = res.choices[0].messages
    MSGS.append(res_message)

    speak(res_message.content)


    # step 3:
    def speak(text):
        # give the AI our voice msg
        speech = gTTS(text=text, lang='en', slow=False)

        speech.save('captured_voice.mp3')
        playsound('captured_voice.mp3')

        os.remove('captured_voice.mp3')
        # time for our AI to listen again 
        listen()

# call the function and assign it to the query variable
query = listen()

# step 4: Install remaining dependencies before running it
# pip instll PyObjC, pyaudio

# step 5: log in to open ai chat gpt
# go to API keys and copy your key then paste it into the string on line 24 openai.ai_key = ''
