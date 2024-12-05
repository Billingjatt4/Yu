from config import *
from pyrogram import Client
from pytgcalls import PyTgCalls


# Bot Client
bot = Client(
    name="Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="CakeMusic/plugins"),  # Folder containing plugins
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
