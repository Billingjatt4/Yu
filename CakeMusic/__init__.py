from typing import Union, List, Pattern
from pyrogram import Client, filters as pyrofl
from config import *
import os
import glob



app = Client(
    name="Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


# Dynamically load plugins
PLUGIN_DIR = "plugins"
for plugin_file in glob.glob(f"{PLUGIN_DIR}/*.py"):
    plugin_name = os.path.basename(plugin_file)[:-3]
    if plugin_name != "__init__":
        __import__(f"{PLUGIN_DIR}.{plugin_name}")

def cdx(commands: Union[str, List[str]]):
    return pyrofl.command(commands, ["/", "!", "."])


def cdz(commands: Union[str, List[str]]):
    return pyrofl.command(commands, ["", "/", "!", "."])


def rgx(pattern: Union[str, Pattern]):
    return pyrofl.regex(pattern)
    
