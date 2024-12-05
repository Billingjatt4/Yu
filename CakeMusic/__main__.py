import asyncio, logging, sys, os
from pyrogram import idle  
from CakeMusic import bot, app, call
from CakeMusic.plugins import ALL_MODULES

loop = asyncio.get_event_loop()

LOGGER = logging.getLogger("YukkiMusic")

async def main():
      LOGGER.info("✅ All Directories Updated.")
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
    try:
        await app.join_chat("HEROKUBIN_01")
        await app.join_chat("HEROKUBIN_01")
    except Exception:
        pass
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

if __name__ == "__main__":
    loop.run_until_complete(main())
