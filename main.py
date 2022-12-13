import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5938941990:AAHsdXJ6f_mQtGnWd5RdVHZ5SXAjZ_BMOaE'

wikipedia.set_lang("ru")
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#1-handler start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, Добро пожаловать в бот википедии!")
#2-handler help
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Этот бот отображает информацию с сайта Wikipedia")

#3-handler umumiy
@dp.message_handler()
async def echo(message: types.Message):

    matn = message.text
    try:
        javob = wikipedia.summary(matn)
        await message.answer(javob)
    except:
        await message.answer("Для этой статьи ничего не найдено")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)