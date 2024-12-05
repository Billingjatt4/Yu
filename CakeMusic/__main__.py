import os, logging, asyncio
from CakeMusic import app as bot
from CakeMusic.plugins.play import app, call
from logging.handlers import RotatingFileHandler
from pyrogram import idle, Client, filters
from config import *


loop = asyncio.get_event_loop()

logging.basicConfig(
    format="[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10),
        logging.StreamHandler(),
    ],
)


logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

LOGGER = logging.getLogger("SYSTEM")

async def main():
    LOGGER.info("🐬 Updating Directories ...")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    if "cookies.txt" not in os.listdir():
        LOGGER.info("⚠️ 'cookies.txt' - Not Found❗")
        sys.exit()
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    for file in os.listdir():
        if file.endswith(".session"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session-journal"):
            os.remove(file)
    LOGGER.info("✅ All Directories Updated.")
    await asyncio.sleep(1)
    LOGGER.info("🌐 Checking Required Variables ...")
    if not API_ID:
        LOGGER.info("❌ 'API_ID' - Not Found ‼️")
        sys.exit()
    if not API_HASH:
        LOGGER.info("❌ 'API_HASH' - Not Found ‼️")
        sys.exit()
    if not BOT_TOKEN:
        LOGGER.info("❌ 'BOT_TOKEN' - Not Found ‼️")
        sys.exit()
    if not STRING_SESSION:
        LOGGER.info("❌ 'STRING_SESSION' - Not Found ‼️")
        sys.exit()

    if not MONGO_DB_URL:
        LOGGER.info("'MONGO_DB_URL' - Not Found !!")
        sys.exit()
 #   try:
     #   await mongo_async_cli.admin.command('ping')
#    except Exception:
   #     LOGGER.info("❌ 'MONGO_DB_URL' - Not Valid !!")
    #    sys.exit()
    LOGGER.info("✅ Required Variables Are Collected.")
    await asyncio.sleep(1)
    LOGGER.info("🌀 Starting All Clients ...")
    try:
        await bot.start()
    except Exception as e:
        LOGGER.info(f"🚫 Bot Error: {e}")
        sys.exit()
    if LOG_GROUP_ID != 0:
        try:
            await bot.send_message(LOG_GROUP_ID, "**🤖 Bot Started.**")
        except Exception:
            pass
    LOGGER.info("✅ Bot Started.")
    try:
        await app.start()
    except Exception as e:
        LOGGER.info(f"🚫 Assistant Error: {e}")
        sys.exit()
    if LOG_GROUP_ID != 0:
        try:
            await app.send_message(LOG_GROUP_ID, "**🦋 Assistant Started.**")
        except Exception:
            pass
    LOGGER.info("✅ Assistant Started.")
    try:
        await call.start()
    except Exception as e:
        LOGGER.info(f"🚫 PyTgCalls Error: {e}")
        sys.exit()
    LOGGER.info("✅ PyTgCalls Started.")
    await asyncio.sleep(1)
    LOGGER.info("✅ Sucessfully Hosted Your Bot !!")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(main())
