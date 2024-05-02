import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
import texts as tx

dp = Dispatcher()


button_start = [
    [types.KeyboardButton(text="Начать работу")],
]

