from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards.default.users import main_menu_keyboard, users_menu_keyboard, settings_keyboard, feedbact_keyboard, \
    languages, users_menu_keyboard_with_lang
from loader import dp
import handlers, middlewares, filters
from loader import _



@dp.message_handler(text=["Menu 🌯", "Menu 🌯", "Меню 🌯"])
async def main_menu_handler(message: Message):
    text = _("Siz menuni tanladingiz")
    await message.answer(text=text, reply_markup= await main_menu_keyboard())


