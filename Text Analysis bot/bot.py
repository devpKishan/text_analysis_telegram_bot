# bot.py
import telebot
from config import BOT_TOKEN
from commands import register_commands

# Initialize bot with the token
bot = telebot.TeleBot(BOT_TOKEN)

# Register command handlers
register_commands(bot)

# Start polling
bot.polling()
