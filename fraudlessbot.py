import telebot
import os

from flask import Flask
from flask import request
from settings import teleBot
from handlers import handlers

apiKey = os.getenv("API_KEY")
webHookHostname = os.getenv("NGROK_HOSTNAME")

app = Flask(__name__)

app.register_blueprint(handlers)


@app.route(f"/{apiKey}", methods=["POST"])
def getMessage():
    jsonString = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(jsonString)
    teleBot.process_new_updates([update])
    return "!", 200


@app.route("/", methods=["GET", "HEAD", "POST"])
def webhook():
    teleBot.remove_webhook()
    teleBot.set_webhook(url=f"https://{webHookHostname}/{apiKey}")
    return "!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv('PORT', 6000)))