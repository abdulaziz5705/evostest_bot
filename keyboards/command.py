from aiogram.types import InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from loader import _

async def phone_number_keyboard(language: str):
    markup = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("Raqamni yuborish", locale=language), request_contact=True)
        ]
        ], resize_keyboard=True,)
    return markup