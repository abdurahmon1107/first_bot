import logging
from aiogram import Bot, Dispatcher, executor, types

# Logging konfiguratsiyasini sozlaymiz
logging.basicConfig(level=logging.INFO)


# Botni yaratamiz
bot = Bot(token="6393805195:AAF-vADpae3Wt3YTxByfvKLJ7DLk8dYux3Q")

# Dispatcher obyektini yaratamiz
dp = Dispatcher(bot)

# Start komandasiga javob berish
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Salom! Men botman. Qanday yordam bera olishim mumkin?")

# Salom so'ziga javob berish
@dp.message_handler(lambda message: "salom" in message.text.lower())
async def salom(message: types.Message):
    await message.reply("Salom! Qanday yordam bera olishim mumkin?")

# Hayr so'ziga javob berish
@dp.message_handler(lambda message: "hayr" in message.text.lower())
async def hayr(message: types.Message):
    await message.reply("Xayr, yana kutib qolaman!")

# Noma'lum so'zlar uchun javob berish
@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Kechirasiz, men tushunmadim. Iltimos, qaytadan yozing yoki boshqa savol berib ko'ring.")

# Pollingni boshlash
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)