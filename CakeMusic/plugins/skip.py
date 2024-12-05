# skip function

@bot.on_message(cdx(["skip", "vskip"]) & ~pyrofl.private)
async def skip_and_change_stream(client, message):
    chat_id = message.chat.id
    try:
        await message.delete()
    except Exception:
        pass
    try:
        call_status = await get_call_status(chat_id)
        if call_status == "IDLE" or call_status == "NOTHING":
            return await bot.send_message(chat_id, "**❎ Nothing Streaming❗...**")
        elif call_status == "PLAYING" or call_status == "PAUSED":
            stickers = [
                "🌹",
                "🌺",
                "🎉",
                "🎃",
                "💥",
                "🦋",
                "🕊️",
                "❤️",
                "💖",
                "💝",
                "💗",
                "💓",
                "💘",
                "💞",
            ]
            aux = await message.reply_text(random.choice(stickers))
            await change_stream(chat_id)
            try:
                await aux.delete()
            except Exception:
                pass
    except Exception as e:
        try:
            await bot.send_message(chat_id, f"**🚫 Skip Error:** `{e}`")
        except Exception:
            LOGGER.info(f"🚫 Skip Error: {e}")
            return
