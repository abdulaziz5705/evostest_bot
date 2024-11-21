
from aiogram.types import Message

from keyboards.default.users import  settings_keyboard
from loader import _, dp

@dp.message_handler(text=["Sozlamalar ⚙️","Настройка ⚙️", "Settings ⚙️"])
async def main_menu_handler(message: Message):
    text = _("Sozlamalar")
    await message.answer(text=text, reply_markup= await settings_keyboard())