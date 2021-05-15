from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**selam , Ben {bn} 🎵

Grubunuzun sesli aramasında müzik çalabilirim. [EfsaneStar](https://t.me/EfsaneStar) tarafından geliştirilmiştir.
Şu anda desteklediğim komutlar şunlardır:
▶️ /oynat - __Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.__
⏸️ /durdur - __Sesli Sohbet Müziğini Duraklat.__
⏩ /devam - __Sesli Sohbet Müziğine Devam Et.__
⏭️ /atla - __Sesli Sohbette Çalan Geçerli Müziği Atlar.__
🛑 /bitir - __Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.__
🔎 /bul - __Müziği bulup gruba gönderir. Örnek /Bul uzi kervan.__
↘️ /katil - __Müzik Botunun Asistanını Gruba Çağırır.__
↘️ /ayril - __Müzik Botunun Asistanını Gruptan Çıkartır.__

Beni grubunuza ekleyin ve özgürce müzik çalın !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👤 Owner 🇹🇷", url="https://t.me/EfsaneStar")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/sohbetskyfall"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/kanalEfsanestar"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⚒️ Destek Group ⚒️", url="https://t.me/Sohbetlobisi"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/kanalEfsanestar")
                ]
            ]
        )
   )


