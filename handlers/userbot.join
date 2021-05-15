from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor group first</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "SerenityHelper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Taşan Bekleme Hatası 🛑 \n Kullanıcı {user.first_name} userbot için yoğun katılım istekleri nedeniyle grubunuza katılamadı! Kullanıcının grupta yasaklı olmadığından emin olun."
            "\n\nOr manually add @SerenityHelper to your Group and try again</b>",
        )
        return
    await message.reply_text(
            "<b>helper userbot joined your chat</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return
