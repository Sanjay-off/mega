import telebot
import time
from config import BOT_TOKEN, CHANNEL_ID

bot = telebot.TeleBot(BOT_TOKEN)

def upload_to_telegram(zip_files):
    for idx, file in enumerate(zip_files, 1):
        with open(file, "rb") as f:
            bot.send_document(
                CHANNEL_ID,
                f,
                caption=f"{file.name}\nPart {idx}/{len(zip_files)}\nPassword: Pinned",
                disable_notification=True
            )
        time.sleep(10)
