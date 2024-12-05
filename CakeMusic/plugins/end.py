
# end function

@bot.on_message(cdx(["end", "vend"]) & ~pyrofl.private)
async def stop_stream_and_leave_vc(client, message):
    chat_id = message.chat.id
    try:
        await message.delete()
    except Exception:
        pass
    try:
        call_status = await get_call_status(chat_id)
        if call_status == "NOTHING":
            return await message.reply_text("**❎ Nothing Streaming❗**")
        elif call_status == "IDLE":
            return await message.reply_text("**✅ Succesfully Left From VC❗**")
        elif call_status == "PLAYING" or call_status == "PAUSED":
            await close_stream(chat_id)
            return await message.reply_text("**❎ Stopped Stream & Left\nFrom VC❗...**")
        else:
            return
    except Exception as e:
        try:
            await bot.send_message(chat_id, f"**🚫 Stream End Error:** `{e}`")
        except Exception:
            LOGGER.info(f"🚫 Stream End Error: {e}")
            return
