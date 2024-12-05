import logging
from CakeMusic import bot
from CakeMusic.plugins.play import app, call
from logging.handlers import RotatingFileHandler
from pyrogram import idle, Client, filters


# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



# Run the bot
if __name__ == "__main__":
    logger.info("Bot is starting...")
    bot.run()
