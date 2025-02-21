from pyrogram import Client, filters
from decouple import config
from pyrogram.types import Message

api_id = config('API_ID')
api_hash = config('API_HASH')
phone = config('PHONE')
login = config('LOGIN')


bot = Client(name=login, api_id=api_id, api_hash=api_hash, phone_number=phone)

@bot.on_message(filters.command('start'))
async def echo_handler(client: Client, message: Message):
    await message.reply(f"Привет. Это бот, который найдет все возможные путешествия"
                        f" по выбранному направлению")


@bot.on_message(filters.text)
async def message_handler(client: Client, message: Message):
    if "путешествие" in message.text.lower():
        await client.send_message(chat_id=1856009970, text = f"{message.text}")

#запуск бота
bot.run()