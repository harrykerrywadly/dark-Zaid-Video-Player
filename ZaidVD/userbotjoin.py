# Copyright (C) 2021 Zaid Music
#Ur Motherfucker If U Kang And Don't Give Creadits π₯΄ π­ππΌππΏ

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.raw.types import InputGroupCall
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, GetGroupCall
from helpers.filters import command
from helpers.decorators import authorized_users_only, errors
from ZaidVD.videoplayer import app as USER
from config import Zaid


@Client.on_message(command(["vjoin", f"userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def entergroup(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>π‘ promote me as admin first to do that !</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "assistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "π€: i'm joined here for streaming video on video chat")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>β assistant already entered this group</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>π΄ FLOODWAIT ERROR π΄\n\n user {user.first_name} couldn't join your group due to heavy join requests for userbot! make sure assistant is not banned in this group."
        )
        return
    await message.reply_text(
        "<b>β assistant userbot joined your chat</b>",
    )


@Client.on_message(command(["vleave", f"userbotleave"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leavegroup(client, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "<b>β assistant can't leave from group because floodwaits.\n\nΒ» you can manually kick me from this group</b>"
        )

        return


@Client.on_message(command(["leaveall", f"userbotleaveall"]))
async def outall(client, message):
    if message.from_user.id not in Veez.SUDO_USERS:
        return

    left=0
    failed=0
    lol = await message.reply("π assistant leaving all chats")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(f"π assistant leaving...\n Left: {left} chats.\n\nβ Failed: {failed} chats.")
        except:
            failed += 1
            await lol.edit(f"π assistant leaving...\nLeft: {left} chats.\n\nβ Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"β Left {left} chats.\n\nβ Failed {failed} chats.")
