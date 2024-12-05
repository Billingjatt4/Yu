# Log All Streams


async def stream_logger(
    chat_id, user, title, duration, stream_type, thumbnail, position=None
):
    if LOG_GROUP_ID != 0:
        if chat_id != LOG_GROUP_ID:
            chat = await bot.get_chat(chat_id)
            chat_name = chat.title
            if chat.username:
                chat_link = f"@{chat.username}"
            else:
                chat_link = "Private Chat"
            try:
                if user.username:
                    requested_by = f"@{user.username}"
                else:
                    requested_by = user.mention
            except Exception:
                requested_by = user.title
            if position:
                caption = f"""**✅ Added To Queue At :** `#{position}`

**🥀 Title:** {title}
**🐬 Duration:** {duration}
**🦋 Stream Type:** {stream_type}
**🌺 Chat Name:** {chat_name}
**🌼 Chat Link:** {chat_link}
**👾 Requested By:** {requested_by}"""
            else:
                caption = f"""**✅ Started Streaming On VC.**

**🥀 Title:** {title}
**🐬 Duration:** {duration}
**🦋 Stream Type:** {stream_type}
**🌺 Chat Name:** {chat_name}
**🌼 Chat Link:** {chat_link}
**👾 Requested By:** {requested_by}"""
            try:
                await bot.send_photo(LOG_GROUP_ID, photo=thumbnail, caption=caption)
            except Exception:
                pass
