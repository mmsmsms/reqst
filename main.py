import os
from telegram.ext import Application, CommandHandler

# توکن ربات رو از Environment Variable می‌گیریم
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# دستور /start
async def start(update, context):
    await update.message.reply_text("سلام! ربات روشنه 🚀")

def main():
    # ساخت اپلیکیشن تلگرام
    application = Application.builder().token(BOT_TOKEN).build()

    # اضافه کردن دستور
    application.add_handler(CommandHandler("start", start))

    # اجرا
    application.run_polling()

if __name__ == "__main__":
    main()
