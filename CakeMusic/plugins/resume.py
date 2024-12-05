
# resume function

@bot.on_message(cdx(["resume", "vresume"]) & ~pyrofl.private)
async def resume_paused_stream_on_vc(client, message):
    chat_id = message.chat.id
    try:
        await message.delete()
    except Exception:
        pass
    try:
        call_status = await get_call_status(chat_id)
        if call_status == "IDLE" or call_status == "NOTHING":
            return await message.reply_text("**❎ Nothing Streaming❗**")

        elif call_status == "PLAYING":
            return await message.reply_text("**🔊 Already Streaming❗**")
        elif call_status == "PAUSED":
            await call.resume_stream(chat_id)
            return await message.reply_text("**🔊 Stream Resumed❗**")
        else:
            return
    except Exception as e:
        try:
            await bot.send_message(chat_id, f"**🚫 Stream Resume Error:** `{e}`")
        except Exception:
            LOGGER.info(f"🚫 Stream Resume Error: {e}")
            return
