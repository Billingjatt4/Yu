from config import *
from pyrogram import Client


# Bot Client
bot = Client(
    name="Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Assistant Client
app = Client(
    name="Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=str(STRING_SESSION),
)

# Py-TgCalls Client
call = PyTgCalls(app)
