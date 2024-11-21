from aiogram.dispatcher import FSMContext

import handlers, middlewares, filters
from aiogram.types import Message

from keyboards.default.users import languages, users_menu_keyboard_with_lang
from loader import _, dp


@dp.message_handler(text=["Orqaga ⬅️", "Назад ⬅️", "Back ⬅️"])
async def main_menu_handler(message: Message , state: FSMContext):
    data = await state.get_data()
    language = data.get('language')
    text = _("Quydagilardan  bittasini tanlashingiz mumkun 👇", locale = language)
    await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))



