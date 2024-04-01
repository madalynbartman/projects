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

