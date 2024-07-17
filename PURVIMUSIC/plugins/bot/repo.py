from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PURVIMUSIC import app
from config import BOT_USERNAME
from PURVIMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓᴄσмє fσʀ Ⓘ︎Ⓢ︎Ⓣ︎Ⓚ︎Ⓗ︎Ⓐ︎Ⓡ︎ ʀєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/VeenaMusic_bot?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/Veena_Networks"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/ll_ISTKHAR_lll"),
          ],
              
[
              InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/TEAMPURVI/ALPHA_USERBOT"),
              InlineKeyboardButton("︎🥀𝆺𝅥⃝❤️‍🔥𝐕ᴇᴇɴᴀ ✘ 𝐌ᴜꜱɪᴄ🫧", url=f"https://github.com/istkharalam62/VEENAMUSIC"),
              ],
  
[
InlineKeyboardButton("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧", url=f"https://github.com/TEAMPURVI/ALPHA_SPAM"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/TEAMPURVI/PURVI_CHAT"),
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/47114db1ce7d5a4138ef0.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="."))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://github.com/istkharalam62/VEENAMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/istkharalam62/VEENAMUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/Veena_Networks)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


