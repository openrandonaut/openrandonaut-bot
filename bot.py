from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
import openrandonaut
from telegram import ReplyKeyboardRemove


updater = Updater(token="TELEGRAM_TOKEN_HERE", use_context=True)


dispatcher = updater.dispatcher

import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="USAGE: Share you location."
    )


def caps(update, context):
    # text_caps = " ".join(context.args).upper()
    for i in context.args:
        context.bot.send_message(chat_id=update.effective_chat.id, text=i)


def got_location(update, context):
    gps = update.message.location
    print("Latitude: {}, Longitude: {}".format(gps.latitude, gps.longitude))

    text = f"Please wait..."
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    reply = openrandonaut.main_generate_location(
        gps.latitude, gps.longitude, 5000, 4096
    )
    text = f"Coordinate based on gaussian kernel density estimate of {reply[3]} QRNG data points, within a radius of {reply[2]}m from your shared location:"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    link = f"http://maps.google.com/maps?q={reply[0]},{reply[1]}"
    context.bot.send_location(
        chat_id=update.effective_chat.id, latitude=reply[0], longitude=reply[1]
    )


start_handler = CommandHandler("start", start)

dispatcher.add_handler(start_handler)


dispatcher.add_handler(MessageHandler(Filters.location, got_location))

updater.start_polling()
