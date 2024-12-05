from pyrogram import Client, filters
from pyrogram.types import Message
import time
from CakeMusic import bot

@bot.on_message(filters.command("ping") & filters.private)
async def ping(client: Client, message: Message):
    start_time = time.time()
    sent_message = await message.reply_text("Pinging...")
    end_time = time.time()
    
    # Calculate response time
    response_time = (end_time - start_time) * 1000  # in milliseconds

    await sent_message.edit_text(
        f"🏓 Pong!\n"
        f"Response Time: `{response_time:.2f} ms`\n"
        f"Bot Uptime: `{await get_bot_uptime(client)}`"
    )

async def get_bot_uptime(client: Client) -> str:
    """
    Calculate the bot's uptime.
    """
    uptime_seconds = time.time() - client.start_time
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
