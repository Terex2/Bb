import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app

@app.on_message(filters.command(["الرابط","/link"], "") & filters.group & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("وخر، شلون تبيني أعطيك رابط المجموعة وأنا مو مشرف؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")
    
