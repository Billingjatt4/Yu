

# pause function


@bot.on_message(cdx(["pause", "vpause"]) & ~pyrofl.private)
async def pause_running_stream_on_vc(client, message):
    chat_id = message.chat.id
    try:
        await message.delete()
    except Exception:
        pass
    try:
        call_status = await get_call_status(chat_id)
        if call_status == "IDLE" or call_status == "NOTHING":
            return await message.reply_text("**❎ Nothing Streaming❗**")

        elif call_status == "PAUSED":
            return await message.reply_text("**🔈 Already Paused❗**")
        elif call_status == "PLAYING":
            await call.pause_stream(chat_id)
            return await message.reply_text("**🔈 Stream Paused❗**")
        else:
            return
    except Exception as e:
        try:
            await bot.send_message(chat_id, f"**🚫 Stream Pause Error:** `{e}`")
        except Exception:
            LOGGER.info(f"🚫 Stream Pause Error: {e}")
            return
