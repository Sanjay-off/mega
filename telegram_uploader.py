import telebot
from config import BOT_TOKEN, CHANNEL_ID

bot = telebot.TeleBot(BOT_TOKEN)

def upload_zips(zip_files: list):
    for index, zip_file in enumerate(zip_files, start=1):
        caption = (
            f"📦 {zip_file.name}\n"
            f"Part {index}/{len(zip_files)}\n"
            f"Password: (Pinned)"
        )

        with open(zip_file, "rb") as f:
            bot.send_document(
                chat_id=CHANNEL_ID,
                document=f,
                caption=caption,
                disable_notification=True
            )
