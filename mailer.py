from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import InputPeerChat
import random
captcha = random.randint(100000, 999999)
import config
maintext = """

 _____                                   _     _____ _____ _   _______ 
/  __ \                                 | |   /  ___|  ___| \ | |  _  \
| /  \/ ___  _ __   __ _ _   _  ___  ___| |_  \ `--.| |__ |  \| | | | |
| |    / _ \| '_ \ / _` | | | |/ _ \/ __| __|  `--. \  __|| . ` | | | |
| \__/\ (_) | | | | (_| | |_| |  __/\__ \ |_  /\__/ / |___| |\  | |/ / 
 \____/\___/|_| |_|\__, |\__,_|\___||___/\__| \____/\____/\_| \_/___/  
                      | |                                              
                      |_|                                              

My Telegram: @conquestcoder
My Github: https://github.com/Conquestcoder
"""

client = TelegramClient(config.session, config.api_id, config.api_hash)

async def main():
    await client.start()
    
    
    async for dialog in client.iter_dialogs():
        if dialog.is_group: 
            try:
                
                chat = dialog.entity
                
                await client(SendMessageRequest(InputPeerChat(chat.id), f"{config.text}"))
                print(f"Succes in: {dialog.title}")
            except Exception as e:
                print(f"cant send a message into: {dialog.title}: {e}")




print(maintext)
print("————————")
print(captcha)
answertocaptcha = input("enter the numbers you see on the screen: ")
if answertocaptcha == f"{captcha}":
	with client:
			client.loop.run_until_complete(main())
else:
	print("you lose the captcha •∆•")
	exit
		