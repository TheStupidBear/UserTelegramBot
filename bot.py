from pyrogram import Client, filters
from decouple import config
from pyrogram.types import Message

api_id = config('API_ID')
api_hash = config('API_HASH')
phone = config('PHONE')
login = config('LOGIN')

travel_list = ['акция', 'кишинев', 'яссы']

bot = Client(name=login, api_id=api_id, api_hash=api_hash, phone_number=phone)

@bot.on_message(filters.command('start'))
async def echo_handler(client: Client, message: Message):
    await message.reply(f"Привет. Это user бот, который найдет все возможные путешествия."
                        f"\nБот ищет в группах все совпадения со словами в списке."
                        f"\n/list - команда вывода списка"
                        f"\nadd ... - добавить в список (add прага)"
                        f"\ndel ... - удалить из списка (del прага)"
                        f"\n/help - повторить все команды")

@bot.on_message(filters.command('help'))
async def echo_handler(client: Client, message: Message):
    await message.reply(f"Бот ищет в группах все совпадения со словами в списке."
                        f"\n/list - команда вывода списка"
                        f"\nadd ... - добавить в список (add прага)"
                        f"\ndel ... - удалить из списка (del прага)")



@bot.on_message(filters.command('list'))
async def echo_handler(client: Client, message: Message):
    await message.reply(f"{travel_list}")

@bot.on_message(filters.chat(1856009970))
async def echo_handler(client: Client, message: Message):
    global travel_list
    mes = message.text.lower()
    if 'del' in mes:
        #разбиваем строку на отдельные слова
        list_mes = mes.split()
        if list_mes[1] in travel_list:
            #удаляем из списка значение
            travel_list.remove(list_mes[1])
            await message.reply(f"Удалено из списка. \nНовый список:{travel_list}")
        else:
            await message.reply(f"Нет такого значения")
    elif 'add' in mes:
        list_mes = mes.split()
        travel_list.append(list_mes[1])
        await message.reply(f"Добавлено в список. \nНовый список:{travel_list}")



@bot.on_message(filters.channel)
async def message_handler(client: Client, message: Message):
    chat_id = 1856009970
    text_mess = message.text
    if text_mess is None:
        text_mess = message.caption.lower()
    else:
        text_mess = message.text.lower()

    if any(item in text_mess for item in travel_list) == True:
        await client.send_message(chat_id=chat_id, text = f"{text_mess}")

#запуск бота
bot.run()