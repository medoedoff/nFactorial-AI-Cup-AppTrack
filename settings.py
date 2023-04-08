import telebot
import os


from dotenv import load_dotenv

load_dotenv()

teleBot = telebot.TeleBot(os.getenv("API_KEY"))
