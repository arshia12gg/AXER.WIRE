from telethon.sync import TelegramClient, events

api_id = 123456      # جایگزین کن
api_hash = 'abcd1234efgh5678ijkl9012mnop3456'  # جایگزین کن
phone_number = '+989123456789'  # از فرم HTML بگیر

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    
    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        if event.is_private:  # فقط در پی‌وی پاسخ بده
            await event.respond('پس از آنلاین شدن جواب میدم✅\nممنون از صبر شما ❤️🤝🏼\nARSHIA')

    await client.run_until_disconnected()

client.loop.run_until_complete(main())
