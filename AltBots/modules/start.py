from telethon import version, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [
        Button.inline("• 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 •", data="help_back")
    ],
    [
        Button.url("•  𝗖𝗛𝗔𝗡𝗡𝗘𝗟 •", "https://t.me/The_castless"),
        Button.url("• 𝐀ηѕн ☸ •", "https://t.me/ansh_xd8")
    ],
    [
        Button.url("• 𝐑єᏢ̶o ☸ •", "https://github.com/anshxD8/ALSPSM")
    ]
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = (
            "╔═════════════════════╗\n"
            "║ ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id}) ║\n"
            "║━━━━━━━━━━━━━━━━━━━║\n"
            "║ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝗢𝗫𝗬𝗚𝗘𝗡](https://t.me/ansh_xd8) ║\n"
            "║━━━━━━━━━━━━━━━━━━━║\n"
            "║ xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ : M3.3 ║\n"
            "║ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.11.3 ║\n"
            "║ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {version} ║\n"
            "╚═════════════════════╝"
        )
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/ab4cd596e018d4bc5be22.jpg6009389784",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
