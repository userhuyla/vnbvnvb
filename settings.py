import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = os.getenv("TELEGRAM_SUPPORT_CHAT_ID")
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "Приветствуем тебя в подслушке Гимназии 85!Если ты еще не присоединился(-ась) к нашему основному каналу, где мы будем выкладывать ваши сплетни и слухи, то сделай это по ссылке (https://t.me/joinchat/lpuU5A_9PN5hODE6) .Чтобы ваше сообщение было опубликовано в группу,просто отправьте его сюда. Это совершенно новый формат подслушки для нашей школы. Все полностью анонимно и конфиденциально. Ваше сообщение будет опубликовано после недлительной модерации. Дабы избежать нарушение закона и не получить пиздюлей, мы тщательно проверяем сообщения на наличие непристойного, подозрительного контента.С любовью, подслушка 85 гимназии❤️")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")
