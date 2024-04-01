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
from gtts import gtts
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
        query = r.recognize_google(audio, 'en-in')
        print(f'user has said {query}')
        messages_array.append({'role': 'user', 'content': query})
        respond(audio)
    except: 
        print('Say that again please..') # because we didn't get any audion so that print handles that exception

# step 2: create a function to respond to new conversation item
def respond(audio):
    print('Responding..') # let's us know the AI is responding


