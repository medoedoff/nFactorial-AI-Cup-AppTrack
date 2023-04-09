import os
import requests
import speech_recognition as sr

from settings import teleBot
from flask import Blueprint
from models import CohereClassification
from pydub import AudioSegment

@teleBot.message_handler(commands=["start"])
def sendMessage(message):
    teleBot.send_message(message.chat.id, "Greetings! Send me your suspicious message")

@teleBot.message_handler(func=lambda message: True)
def messageFromUser(message):
    cohereClassification = CohereClassification(message=message.text)
    response = cohereClassification.get()
    teleBot.reply_to(message, response)

@teleBot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_id = message.voice.file_id
    file_info = teleBot.get_file(file_id)
    downloaded_file = teleBot.download_file(file_info.file_path)

    with open("voice_message.ogg", "wb") as f:
        f.write(downloaded_file)

    voice_message = AudioSegment.from_ogg("voice_message.ogg")
    voice_message.export("voice_message.wav", format="wav")

    r = sr.Recognizer()

    with sr.AudioFile("voice_message.wav") as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)

    cohereClassification = CohereClassification(message=text)
    response = cohereClassification.get()
    teleBot.reply_to(message, response)

# Convert the handlers instance to a Flask blueprint
handlers = Blueprint("handlers", __name__)