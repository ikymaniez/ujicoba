from config import BOT_NAME as bot_username
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJlR9giNcPJke9BKSpQhP0zaOgf3z-KQACAQADFlyeOsyiWLhvkgt7HwQ")
    await message.reply_text(
        f"""⚜️<b>Hi {message.from_user.first_name} Welcome To 

Aku Adalah Bot Music Telegram Yang Akan Menemani mu Di Voice Call Group.
Jika Ingin Menggunakan Invite Aku Dan Asisstantnya Ke Dalam Group Lalu Angkat Bot Menjadi Admin. Jika Ada Kendala Bisa Chat Pemilik Nya.
┏━━━━━━━━━━━━━━
┣ • Memutar Musik.
┣ • Mendownload Lagu.
┣ • Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━
🤵𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓫𝔂 : [IKYY](https://t.me/boyfriendnice)
☘️𝓣𝓱𝓪𝓷𝓴𝓼 𝓯𝓸𝓻 : [Grup Support](https://t.me/Familythunder)
━━━━━━━━━━━━━━
𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 : @Virtualsong_tbot - 𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐌𝐔𝐒𝐈𝐊 : AsisstantMusicVirtual
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://t.me/MusikManagement/11",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Familythunder"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/MusikManagement"
                    ),
                    InlineKeyboardButton(
                        "🦇 Owner", url="https://t.me/boyfriendnice"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🍀 Instagram", url="https://www.instagram.com/ikyyy_35/"
                    ) 
                ]
            ]
        )
    )
@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/MusikManagement"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!

⚜️Users Commands⚜️
/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly

⚜️Admins only⚜️
/player - open Music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/MusikManagement"
                    )
                ]
            ]
        )
    )    
