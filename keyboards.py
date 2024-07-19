from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Создание клавиатуры
keyboard_dialog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")],
        [KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

inline_keyboard_media = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://news.yandex.ru")],
        [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru")],
        [InlineKeyboardButton(text="Видео", url="https://youtube.com")]
    ]
)

keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
])

keyboard_option = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
    [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
])