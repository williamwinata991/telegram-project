from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import re

key_token = "6799410917:AAFDrnVG3fT1W-T351Q0L2POtpLCgELHGk0"  # Masukkan KEY-TOKEN BOT
user_bot = "BotakBot"  # Masukkan @user bot

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")

async def text_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text
    print(f"Pesan diterima: {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'halo' in text_lwr_diterima:
        await update.message.reply_text("Hallo juga")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text("Selamat malam..., jangan lupa istirahat 😊")
    elif 'siapa kamu ?' in text_lwr_diterima:
        await update.message.reply_text(f"bot adalah : {user_bot}")
    else:
        await update.message.reply_text("bot tidak mengerti")

async def photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")

async def other_photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Terima kasih atas gambar kamu!")

async def check_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text
    # Menggunakan regular expression untuk mendeteksi link
    if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text_diterima):
        await update.message.reply_text("Ini tampak seperti sebuah link!")
    else:
        await update.message.reply_text("Ini bukan link.")

async def delete_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.delete()

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command_list = [
        "/start - Memulai bot",
        "/help - Menampilkan bantuan",
        "/delete - Menghapus pesan",
        "/menu - Menampilkan menu perintah"
    ]
    menu_text = "\n".join(command_list)
    await update.message.reply_text(f"Berikut adalah daftar perintah yang tersedia:\n{menu_text}")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")

if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    # COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('delete', delete_message))
    app.add_handler(CommandHandler('menu', show_menu))
    # MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.TEXT, check_link))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    # error :
    app.add_error_handler(error)
    # polling :
    app.run_polling(poll_interval=1)
