# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import Client, filters

from Bikash import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/3d08fb7b9c3d352f8ff60.jpg",
        caption=f"""🥀 𝐍𝐨𝐰 𝐌𝐲 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐈𝐬 PRIVATE 🌺,𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤, 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 𝐁𝐮𝐭𝐭𝐨𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩""",
        reply_markup=InlineKeyboardMarkup(
            [          
                [
                    InlineKeyboardButton(
                        "🥀 𝐎𝐖𝐍𝐄𝐑 🥀", url=f"/https://t.me/Mr_pr0feSser")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/About_botserver"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/hindi_chattings_zone")
                ]
            ]
        ),
    ) 

# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
