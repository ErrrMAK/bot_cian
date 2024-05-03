
"""
TODO
Finish to save data 
Add save tg_id
"""

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext



import texts as tx
import bot_button as kb

router = Router()

# Определение состояний
class DispetcherState(StatesGroup):
    waiting_for_name = State()
    waiting_for_type_legend = State()
    waiting_for_flat_info = State()  # Состояние для вызова get_flat

# Старт диалога
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb.button_start,
        resize_keyboard=True
        )
    await message.answer(tx.text_start, reply_markup=keyboard)

@router.message(F.text.lower() == "начать работу")
async def with_puree(message: Message, state: FSMContext):
    await state.set_state(DispetcherState.waiting_for_name)
    await message.answer("Напишите Ваше имя для диалога:")


# Обработчик для получения имени
@router.message(DispetcherState.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(DispetcherState.waiting_for_type_legend)
    await message.answer(tx.legend_type, reply_markup=kb.button_type_legend)

# Обработчик для получения типа легенды
@router.callback_query(DispetcherState.waiting_for_type_legend)
async def get_legend(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    await state.update_data(type_legend=query.data)

    user_data = await state.get_data()
    name = user_data['name']
    type_legend = user_data['type_legend']
    await state.set_state(DispetcherState.waiting_for_flat_info)
    # await state.clear()  # Очищаем состояние
