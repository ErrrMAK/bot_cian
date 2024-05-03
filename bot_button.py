import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                        InlineKeyboardMarkup, InlineKeyboardButton)

from config import TOKEN
import texts as tx

dp = Dispatcher()


button_start = [
    [types.KeyboardButton(text="Начать работу")],
]

button_type_legend = InlineKeyboardMarkup(
    inline_keyboard=
[
    [
        InlineKeyboardButton(text='Покупатель', callback_data='Покупатель'),
        InlineKeyboardButton(text='Агент', callback_data='Агент'),
    ]
])

