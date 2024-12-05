

# play function

@bot.on_message(cdz(["play", "vplay"]) & ~pyrofl.private)
async def stream_audio_or_video(client, message):
    try:
        await message.delete()
    except Exception:
        pass
    chat_id = message.chat.id
    await add_served_chat(chat_id)
    user = message.from_user if message.from_user else message.sender_chat
    replied = message.reply_to_message
    audio = (replied.audio or replied.voice) if replied else None
    video = (replied.video or replied.document) if replied else None
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
    if audio:
        title = "Unsupported Title"
        duration = "Unknown"
        try:
            stream_file = await replied.download()
        except Exception:
            return
        result_x = None
        stream_type = "Audio"

    elif video:
        title = "Unsupported Title"
        duration = "Unknown"
        try:
            stream_file = await replied.download()
        except Exception:
            return
        result_x = None
        stream_type = "Video"

    else:
        if len(message.command) < 2:
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🗑️ Close",
                            callback_data="force_close",
                        )
                    ],
                ]
            )
            return await aux.edit_text(
                "**🥀 Give Me Some Query To\nPlay Audio Or Video❗...\n\nℹ️ Examples:\n≽ Audio: `/play satisfya`\n≽ Video: `/vplay satisfya`**",
                reply_markup=buttons,
            )
        query = message.text.split(None, 1)[1]
        if "https://" in query:
            base = r"(?:https?:)?(?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube(?:\-nocookie)?\.(?:[A-Za-z]{2,4}|[A-Za-z]{2,3}\.[A-Za-z]{2})\/)?(?:shorts\/|live\/)?(?:watch|embed\/|vi?\/)*(?:\?[\w=&]*vi?=)?([^#&\?\/]{11}).*$"
            resu = re.findall(base, query)
            vidid = resu[0] if resu[0] else None
        else:
            vidid = None
        url = f"https://www.youtube.com/watch?v={vidid}" if vidid else None
        search_query = url if url else query
        results = VideosSearch(search_query, limit=1)
        for result in (await results.next())["result"]:
            vid_id = vidid if vidid else result["id"]
            vid_url = url if url else result["link"]
            try:
                title = "[" + (result["title"][:18]) + "]" + f"({vid_url})"
                title_x = result["title"]
            except Exception:
                title = "Unsupported Title"
                title_x = title
            try:
                durationx = result.get("duration")
                if not durationx:
                    duration = "Live Stream"
                    duration_x = "Live"
                elif len(durationx) == 4 or len(durationx) == 7:
                    duration = f"0{durationx} Mins"
                    duration_x = f"0{durationx}"
                else:
                    duration = f"{durationx} Mins"
                    duration_x = f"{duration}"
            except Exception:
                duration = "Unknown"
                duration_x = "Unknown Mins"
            try:
                views = result["viewCount"]["short"]
            except Exception:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except Exception:
                channel = "Unknown Channel"
        stream_file = url if url else result["link"]
        result_x = {
            "title": title_x,
            "id": vid_id,
            "link": vid_url,
            "duration": duration_x,
            "views": views,
            "channel": channel,
        }
        stream_type = "Audio" if str(message.command[0][0]) != "v" else "Video"

    try:
        requested_by = user.mention
    except Exception:
        if user.username:
            requested_by = "[" + user.title + "](https://t.me/" + user.username + ")"
        else:
            requested_by = user.title
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🗑️ Close",
                    callback_data="force_close",
                )
            ],
        ]
    )
    if stream_type == "Audio":
        stream_media = MediaStream(
            media_path=stream_file,
            video_flags=MediaStream.Flags.IGNORE,
            audio_parameters=AudioQuality.STUDIO,
            ytdlp_parameters="--cookies cookies.txt",
        )
    elif stream_type == "Video":
        stream_media = MediaStream(
            media_path=stream_file,
            audio_parameters=AudioQuality.STUDIO,
            video_parameters=VideoQuality.HD_720p,
            ytdlp_parameters="--cookies cookies.txt",
        )
    call_status = await get_call_status(chat_id)
    try:
        if call_status == "PLAYING" or call_status == "PAUSED":
            try:
                thumbnail = await create_thumbnail(result_x, user.id)
                position = await add_to_queue(
                    chat_id, user, title, duration, stream_file, stream_type, thumbnail
                )
                caption = f"""**✅ Added To Queue At :** `#{position}`

**🥀 Title:** {title}
**🐬 Duration:** {duration}
**🦋 Stream Type:** {stream_type}
**👾 Requested By:** {requested_by}"""
                await bot.send_photo(chat_id, thumbnail, caption, reply_markup=buttons)
                await stream_logger(
                    chat_id, user, title, duration, stream_type, thumbnail, position
                )
            except Exception as e:
                try:
                    return await aux.edit(f"**Queue Error:** `{e}`")
                except Exception:
                    LOGGER.info(f"Queue Error: {e}")
                    return
        elif call_status == "IDLE" or call_status == "NOTHING":
            try:
                await call.play(chat_id, stream_media, config=call_config)
            except NoActiveGroupCall:
                try:
                    assistant = await bot.get_chat_member(chat_id, app.me.id)
                    if (
                        assistant.status == ChatMemberStatus.BANNED
                        or assistant.status == ChatMemberStatus.RESTRICTED
                    ):
                        try:
                            return await aux.edit_text(
                                f"**🤖 At First, Unban [Assistant ID](https://t.me/{app.me.username}) To Start Stream❗**"
                            )
                        except Exception:
                            LOGGER.info(
                                f"🤖 At First, Unban Assistant ID To Start Stream❗**"
                            )
                            return
                except ChatAdminRequired:
                    try:
                        return await aux.edit_text(
                            "**🤖 At First, Promote Me as An Admin❗**"
                        )
                    except Exception:
                        LOGGER.info("**🤖 At First, Promote Me as An Admin❗**")
                        return
                except UserNotParticipant:
                    if message.chat.username:
                        invitelink = message.chat.username
                        try:
                            await app.resolve_peer(invitelink)
                        except Exception:
                            pass
                    else:
                        try:
                            invitelink = await bot.export_chat_invite_link(chat_id)
                        except ChatAdminRequired:
                            return await aux.edit_text(
                                "**🤖 Hey, I need invite user permission to add Assistant ID❗**"
                            )
                        except Exception as e:
                            try:
                                return await aux.edit_text(
                                    f"**🚫 Assistant Error:** `{e}`"
                                )
                            except Exception:
                                pass
                            LOGGER.info(f"🚫 Assistant Error: {e}")
                            return
                    try:
                        await asyncio.sleep(1)
                        await app.join_chat(invitelink)
                    except InviteRequestSent:
                        try:
                            await bot.approve_chat_join_request(chat_id, adi.me.id)
                        except Exception as e:
                            try:
                                return await aux.edit_text(
                                    f"**🚫 Approve Error:** `{e}`"
                                )
                            except Exception:
                                pass
                            LOGGER.info(f"🚫 Approve Error: {e}")
                            return
                    except UserAlreadyParticipant:
                        pass
                    except Exception as e:
                        try:
                            return await aux.edit_text(
                                f"**🚫 Assistant Join Error:** `{e}`"
                            )
                        except Exception:
                            pass
                        LOGGER.info(f"🚫 Assistant Join Error: {e}")
                        return
                try:
                    await call.play(chat_id, stream_media, config=call_config)
                except NoActiveGroupCall:
                    try:
                        return await aux.edit_text(f"**⚠️ No Active VC❗...**")
                    except Exception:
                        LOGGER.info(f"⚠️ No Active VC ({chat_id})❗... ")
                        return
            except TelegramServerError:
                return await aux.edit_text("**⚠️ Telegram Server Issue❗...**")
            try:
                thumbnail = await create_thumbnail(result_x, user.id)
                position = await add_to_queue(
                    chat_id, user, title, duration, stream_file, stream_type, thumbnail
                )
                caption = f"""**✅ Started Streaming On VC.**

**🥀 Title:** {title}
**🐬 Duration:** {duration}
**🦋 Stream Type:** {stream_type}
**👾 Requested By:** {requested_by}"""
                await bot.send_photo(chat_id, thumbnail, caption, reply_markup=buttons)
                await stream_logger(
                    chat_id, user, title, duration, stream_type, thumbnail
                )
            except Exception as e:
                try:
                    return await aux.edit(f"**Send Error:** `{e}`")
                except Exception:
                    LOGGER.info(f"Send Error: {e}")
                    return
        else:
            return
        try:
            await aux.delete()
        except Exception:
            pass
        await add_active_media_chat(chat_id, stream_type)
        return
    except Exception as e:
        try:
            return await aux.edit_text(f"**Stream Error:** `{e}`")
        except Exception:
            LOGGER.info(f"🚫 Stream Error: {e}")
            return
