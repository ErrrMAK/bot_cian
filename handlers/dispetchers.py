
"""
TODO
Finish to save data 
Add save tg_id
"""

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext



import texts as tx
import bot_button as kb

from aiogram.types import (ReplyKeyboardMarkup, 
                        KeyboardButton, 
                        InlineKeyboardMarkup, 
                        InlineKeyboardButton)

router = Router()

# Определение состояний
class DispetcherState(StatesGroup):
    waiting_for_name = State()
    waiting_for_type_legend = State()
    waiting_for_flat_info = State()  # Состояние для вызова get_flat

# Старт диалога
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(tx.text_start, reply_markup=kb.button_start)

@router.callback_query(F.data == "Начать работу")
async def with_puree(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()  # Подтверждение получения callback
    await state.set_state(DispetcherState.waiting_for_name)
    await callback.message.answer("Напишите Ваше имя для диалога:")


# Обработчик для получения имени
@router.message(DispetcherState.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(DispetcherState.waiting_for_type_legend)
    await message.answer(tx.legend_type, reply_markup=kb.button_type_legend)

# Обработчик для получения типа легенды
@router.callback_query(DispetcherState.waiting_for_type_legend)
async def get_legend(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_legend=callback.data)

    user_data = await state.get_data()
    name = user_data['name']
    type_legend = user_data['type_legend']
    await state.set_state(DispetcherState.waiting_for_flat_info)
    # await state.clear()  # Очищаем состояние


import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.callback_query(DispetcherState.waiting_for_flat_info)
async def get_flat_info(callback: types.CallbackQuery, state: FSMContext):
    logger.info("Entered get_flat_info")
    await callback.message.answer('Ответ отправлен')
    logger.info("Answer sent")
