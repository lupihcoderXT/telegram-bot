from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8552600125:AAFOMeE0flI_u4ppJMyavxeCucZfyONIqvc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    if user.username:
        name = f"@{user.username}"
    else:
        name = user.first_name

    text = f"Halo {name} 👋"

    keyboard = [
        [InlineKeyboardButton("Join Grup", url="https://t.me/linkgrup")],
        [InlineKeyboardButton("Join Channel", url="https://t.me/lurevinsight")],
        [InlineKeyboardButton("Blog", url="https://lurevstore.biz.id")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text, reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot aktif...")
app.run_polling()
