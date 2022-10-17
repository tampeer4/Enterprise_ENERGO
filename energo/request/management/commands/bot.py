from distutils.log import error
from sqlite3 import connect
from urllib import request
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from request.models import Request_Part,Request_Man


def log_errors(f):
    
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner

@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = request.message.chat.id
    text = request.message.text
    reply_text = f'Поступила новая заявка на тему: {chat_id}\n От\n{text}'
    request.message.reply_text(
        text=reply_text,
    )
 
class Command(BaseCommand):
    help = 'Телеграм-бот'




    def handle(self, *args, **options):
        # 1 -- правильное подключение
        request = Request(
            connect_timeout = 0.5,
            read_timeout = 1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )
        print(bot.get_me())
        # 2 -- обработчики
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        message_hadler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_hadler)

        # 3 -- запускается бесконечная обработка входящих сообщений
        updater.start_polling()
        updater.idle()
