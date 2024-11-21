from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from loader import _

async def users_menu_keyboard_with_lang(language: str):
    markup = ReplyKeyboardMarkup(
        [
            [
               KeyboardButton(text=_("Menu 🌯", locale=language))
            ],
            [
                KeyboardButton(text=_("Mening zakazlarim 🛍", locale=language))
            ],
            [
               KeyboardButton(text=_("Fikir qoldirish ✍️",  locale=language)),
               KeyboardButton(text=_("Sozlamalar ⚙️", locale=language))

            ],
        ],
        resize_keyboard=True)
    return markup
async def users_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        [
            [
               KeyboardButton(text="Menu 🌯")
            ],
            [
                KeyboardButton(text="Mening zakazlarim 🛍")
            ],
            [
               KeyboardButton(text="Fikir qoldirish ✍️"),
               KeyboardButton(text="Sozlamalar ⚙️")

            ],
        ],
        resize_keyboard=True)
    return markup
async def main_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Mening manzilim 🗺 "))
            ],
            [
               KeyboardButton(text=_("Lokatsiya junatish 📍")),
               KeyboardButton(text=_("Orqaga ⬅️"))

            ],
        ], resize_keyboard=True
    )
    return markup

async def settings_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Tilni o'zgartirish"))
            ],
            [
                KeyboardButton(text=_("Orqaga ⬅️"))
            ]
        ], resize_keyboard=True
    )
    return markup

async def feedbact_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Xabarni Yuborish"))
            ],
            [
                KeyboardButton(text=_("Orqaga ⬅️"))
            ]
        ], resize_keyboard=True
    )
    return markup

languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇷🇺 Russian"),
            KeyboardButton(text="🇬🇧 English"),
        ]
    ], resize_keyboard=True
)