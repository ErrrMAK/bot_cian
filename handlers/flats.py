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

class Flat(StatesGroup):
    photo = State()


# Обработчик для получения типа легенды
@router.callback_query(DispetcherState.waiting_for_flat_info)
async def get_legend(callback: types.CallbackQuery, state: FSMContext, message: types.Message):
    file_ids = []
    # Отправка файла из файловой системы
    image_from_pc = FSInputFile("pictures/flat/1.jpg")
    result = await callback.message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id)

    text_flat = """
        Ломоносова ул 16, кв /n (КН ?)-4ккв
        5400тр(203тр/м2)-26.5м2(2)=ПП
        эт-3/4(?) Вх-? Ок-? СУ-? Кух-13.8м2(ГАЗ)
        Sкв-95.8м2(?=?%) h=3.7
        ЦИАН (https://spb.cian.ru/sale/flat/294834061/) 08.11 (174дн)
        +79675386779 С-ID 18780353
        МКД-Ц (КН:❓2мкд❗️)
        """

    await state.set_state(Flat.photo)
    await message.answer_photo(
        image_from_pc,
        caption=text_flat,
        reply_markup=kb.button_chose_flat)
