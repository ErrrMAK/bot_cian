from aiogram.types import (ReplyKeyboardMarkup, 
                        KeyboardButton, 
                        InlineKeyboardMarkup, 
                        InlineKeyboardButton)


button_start = InlineKeyboardMarkup(
    inline_keyboard=
    [
    [InlineKeyboardButton(text="Начать работу", callback_data="Начать работу")],
])

button_type_legend = InlineKeyboardMarkup(
    inline_keyboard=
    [
    [
        InlineKeyboardButton(text='Покупатель', callback_data='Покупатель'),
        InlineKeyboardButton(text='Агент', callback_data='Агент'),
    ]
])

button_chose_flat = InlineKeyboardMarkup(
    inline_keyboard=
[
    [
        InlineKeyboardButton(text='<', callback_data='<'),
        InlineKeyboardButton(text='Комнаты', callback_data='Комнаты'),
        InlineKeyboardButton(text='Звонить', callback_data='Звонить'),
        InlineKeyboardButton(text='>', callback_data='>'),
    ]
])
