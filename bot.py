from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8552600125:AAFOMeE0flI_u4ppJMyavxeCucZfyONIqvc"

# command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! 👋\n"
        "Selamat datang di bot share link.\n\n"
        "Gunakan command:\n"
        "/link - untuk mendapatkan link website\n"
        "/help - bantuan"
    )

# command /link
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ini link website kami:\n"
        "https://www.lurevstore.biz.id"
    )

# command /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Daftar command bot:\n"
        "/start - memulai bot\n"
        "/link - mendapatkan link\n"
        "/help - bantuan"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("link", link))
app.add_handler(CommandHandler("help", help))

app.run_polling()