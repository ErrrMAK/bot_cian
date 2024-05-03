from aiogram import F, Router, types, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters.state import StateFilter

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import asyncio
import logging


import texts as tx
import bot_button as kb
from handlers.dispetchers import DispetcherState

router = Router()

class flat():
    photo = ''

# Обработчик для получения типа легенды
@router.callback_query(DispetcherState.waiting_for_flat_info)
async def get_flat(query: types.CallbackQuery, state: FSMContext):
    file_ids = []
    # Отправка файла из файловой системы
    image_from_pc = FSInputFile("pictures/flat/1.jpg")
    result = await query.message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id)