import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Bienvenue sur le bot officiel d’AVLAC !\n\nNous aidons pour :\n- 🎓 Opportunités d’études\n- ✈️ Assistance Visa (AVLAC Visa Consulting)\n- 🛫 Programmes internationaux (Alabuga Start)\n- 📄 Aide pour documents administratifs et visa.\n\nContact : +243972326509\nMail : aviationlimitlessacademy@gmail.com")

bot.polling()
