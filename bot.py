import os
import urllib.request
from setting import API_TOKEN, PING_TIME, IP_LIST, DOMAIN_LIST, CHAT_IDS
import asyncio
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

menu_buttons = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
menu_buttons.row(types.KeyboardButton(text="🔬 Тестирование локальной сети"), types.KeyboardButton(text="🔄 Автоматическое тестирование"))

async def get_ping_result(node):
    response = os.system("ping -c 1 " + node)
    return '\u2705' if response == 0 else '\U0000274c'

async def get_http_response_code(node):
    try:
        response = urllib.request.urlopen(node).getcode()
    except:
        response = 404
    return response

async def send_network_test_results_error():
    error_message = "Следующие серверы недоступны:"
    error_occurred = False

    for node in IP_LIST:
        result = await get_ping_result(node)
        if result == '\U0000274c':
            error_occurred = True
            error_message += f"\n{result} {node}"

    for node in DOMAIN_LIST:
        response = await get_http_response_code(node[0])
        if response != 200:
            error_occurred = True
            error_message += f"\n{result} {node[1]} ({response})"
    
    if error_occurred:
        for chat_id in CHAT_IDS:
            await bot.send_message(chat_id=chat_id, text=error_message, reply_markup=menu_buttons)

@dp.message_handler(text='🔄 Автоматическое тестирование')
async def send_welcome(message: types.Message):
    msg = "Запущенно автоматическое тестирование локальной сети...\nДля остановки тестирования остановите бота на сервере"
    await message.answer(msg, reply_markup=menu_buttons)
    while True:
        await send_network_test_results_error()
        await asyncio.sleep(PING_TIME)

@dp.message_handler(text=['🔬 Тестирование локальной сети'])
async def send_welcome(message: types.Message):
    msg = "Запущенно тестирование локальной сети..."
    await message.answer(msg, reply_markup=menu_buttons)
    answer = "Результат тестирования локальной сети:"
    for node in IP_LIST:
        result = await get_ping_result(node)
        answer += f"\n{result} {node}"
    
    for node in DOMAIN_LIST:
        response = await get_http_response_code(node[0])
        result = '\u2705' if response == 200 else '\U0000274c'
        answer += f"\n{result} {node[1]} ({response})"
    
    await message.reply(answer, reply_markup=menu_buttons)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    msg = "Доброго времени суток! ⭐️\nЯ провожу тестирование локальной сети. 🖥️🔌"
    await message.answer(msg, reply_markup=menu_buttons)

@dp.message_handler()
async def echo(message: types.Message):
    msg = "Доброго времени суток! ⭐️\nЯ провожу тестирование локальной сети. 🖥️🔌"
    await message.answer(msg, reply_markup=menu_buttons)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
