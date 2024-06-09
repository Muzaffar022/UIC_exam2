from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)
import requests
from bs4 import BeautifulSoup

async def holiday(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    request = requests.get(
        f"https://calendarific.com/api/v2/holidays?&api_key=nP5EjQWi9KDHNzVOySuULjOKLdgn6oWW&country=UZ&year=2024")
    resulst = request.json()
    Holiday1 = resulst["response"]["holidays"][0]['name']
    date1 = resulst["response"]["holidays"][0]['date']['iso']
    Holiday2 = resulst["response"]["holidays"][1]['name']
    date2 = resulst["response"]["holidays"][1]['date']['iso']
    Holiday3 = resulst["response"]["holidays"][2]['name']
    date3 = resulst["response"]["holidays"][2]['date']['iso']
    Holiday4 = resulst["response"]["holidays"][3]['name']
    date4 = resulst["response"]["holidays"][3]['date']['iso']
    text = f"Holidays \n{Holiday1} {date1}\n{Holiday2} {date2}\n{Holiday3} {date3}\n{Holiday4} {date4}"
    await update.message.reply_text(text)

app = ApplicationBuilder().token("7309689830:AAHj71Z6-FgsdjJxJVWdiXYCgOKokyaUUso").build()
app.add_handler(CommandHandler("holiday",holiday))






app.run_polling()