import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.reply("Хочешь пообщаться? Выбери способ:", reply_markup=kb.keyboard_dialog)

# Обработчик кнопки "Привет"
@dp.message(F.text == "Привет")
async def say_hello(message: Message):
    user_name = message.from_user.first_name
    await message.reply(f"Привет, {user_name}!")

# Обработчик кнопки "Пока"
@dp.message(F.text == "Пока")
async def say_goodbye(message: Message):
    user_name = message.from_user.first_name
    await message.reply(f"До свидания, {user_name}!")

# Обработчик команды /links
@dp.message(Command("links"))
async def send_links(message: Message):
    await message.reply("Выберите ссылку:", reply_markup=kb.inline_keyboard_media)

# Обработчик команды /dynamic
@dp.message(Command("dynamic"))
async def send_dynamic_button(message: Message):
    await message.answer("Выберите опцию:", reply_markup=kb.keyboard_dynamic)

# Обработчик нажатий на инлайн-кнопки "Показать больше"
@dp.callback_query(F.data == "show_more")
async def choose_option(callback: CallbackQuery):
    await callback.message.edit_text("Выберите опцию:", reply_markup=kb.keyboard_option)

# Обработчик нажатий на кнопки "Опция 1" и "Опция 2"
@dp.callback_query(F.data.in_({"option_1", "option_2"}))
async def handle_option(callback: CallbackQuery):
    option_text = "Опция 1" if callback.data == "option_1" else "Опция 2"
    await callback.message.answer(option_text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
