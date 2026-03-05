import os
import requests
from flask import Flask, request

app = Flask (__name__)
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

@app.route("/")
def index():
  return "Olá, <b>tudo bem?</b>"

@app.route("/teste")
def teste():
  return "Essa página é um <b>teste</b>! Beijos"

@app.route("/telegram", methods=["POST"])
def telegram_update():

    update = request.json

    if "message" not in update:
        return "ok"

    chat_id = update["message"]["chat"]["id"]

    url_envio = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    mensagem = {
        "chat_id": chat_id,
        "text": "mensagem <b>recebida</b>!",
        "parse_mode": "HTML"
    }

    requests.post(url_envio, json=mensagem)

    return "ok"