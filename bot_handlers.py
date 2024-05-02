from aiogram import F, Router, types, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters.state import StateFilter

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import asyncio
import logging


import texts as tx
import bot_button as kb

router = Router()

# Определение состояний
class DialogState(StatesGroup):
    waiting_for_name = State()
    waiting_for_type_legend = State()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb.button_start,
        resize_keyboard=True
        )
    await message.answer(tx.text_start, reply_markup=keyboard)

@router.message(F.text.lower() == "начать работу")
async def with_puree(message: Message, state: FSMContext):
    await state.set_state(DialogState.waiting_for_name)
    await message.answer("Напишите Ваше имя для диалога:")

# Обработчик для получения имени
@router.message(DialogState.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(DialogState.waiting_for_type_legend)
    await message.answer(tx.legend_type)

# Обработчик для получения типа легенды
@router.message(DialogState.waiting_for_type_legend)
async def get_legend(message: Message, state: FSMContext):
    user_data = await state.get_data()
    name = user_data['name']  # Извлекаем сохраненное имя
    legend = message.text  # Сохраняем полученный тип легенды
    # Здесь можно добавить сохранение данных в CSV, если это требуется
    await message.answer(f"Привет, {name}, ваш выбранный тип легенды: {legend}!")
    await state.clear()  # Очищаем состояние
