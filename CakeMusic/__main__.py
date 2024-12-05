import sys, os, logging, asyncio
from CakeMusic import bot
from CakeMusic.plugins.play import app, call
from logging.handlers import RotatingFileHandler
from pyrogram import idle, Client, filters
from config import *


# Run the bot
if __name__ == "__main__":
    logger.info("Bot is starting...")
    bot.run()
