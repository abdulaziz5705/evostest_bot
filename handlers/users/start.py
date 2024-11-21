import handlers
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes, ReplyKeyboardRemove
from loader import _
from keyboards.default.users import languages, users_menu_keyboard_with_lang
from keyboards.command import phone_number_keyboard
from keyboards.default.users import users_menu_keyboard, main_menu_keyboard, settings_keyboard, feedbact_keyboard
from loader import dp
from states.users import RegisterState
from utils.get_lang_code import get_lang_by_text
from utils.get_location import get_full_address
from utils.user_commands.users import get_user, add_user


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    await state.finish()
    user = await get_user(chat_id=message.chat.id)
    language = await get_lang_by_text(language=message.text)
    await state.update_data(language=language)
    if user:
        text = _("Pastagilardan bittasini tanlashingiz mumkun 👇", locale = language)
        await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))
    else:
        text = "🇺🇿 Tilni tanlang\n 🇬🇧 Select Language\n 🇷🇺 Выберите язык"
        await message.answer(text=text, reply_markup=languages)
        await RegisterState.language.set()


@dp.message_handler(state=RegisterState.language)
async def language_handler(message: Message, state: FSMContext):
    language = await get_lang_by_text(language=message.text)
    await state.update_data(language=language)
    text = _("Iltimos ismingizni kiriting ", locale=language)
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.fullname.set()

@dp.message_handler(state=RegisterState.fullname)
async def get_fullname_handler(message: Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    data = await state.get_data()
    language = data.get('language')

    text = _("Iltimos pasdagi kontakt ulashish tugmasini bosing 📞", locale = language)

    await message.answer(text=text, reply_markup= await phone_number_keyboard(language=language))
    await RegisterState.phone_number.set()

@dp.message_handler(state=RegisterState.phone_number, content_types=ContentTypes.TEXT)
async def send_phone_number_handler(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    data = await state.get_data()
    language = data.get('language')
    text = _("❌ Telefon nomer formati xato ", locale = language)
    await message.answer(text=text, reply_markup= await phone_number_keyboard(language=language))
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=ContentTypes.CONTACT)
async def send_phone_number_handler(message: Message, state: FSMContext):
        await state.update_data(phone_number=message.contact.phone_number)
        data = await state.get_data()
        language = data.get('language')
        new_user = await add_user(message=message, data=data)
        if new_user:
            text = _("Muvofaqiyatli ro'yhatdan o'ttingiz  ✅ ", locale = language)
            await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))
            text = _("Quydagilardan  bittasini tanlashingiz mumkun 👇", locale = language)
            await message.answer(text=text, reply_markup= await users_menu_keyboard_with_lang(language=language))

        else:
            text = _("Iltimos kiyenroq urunib ko'ring", locale = language)
            await message.answer(text=text)

        await state.finish()



@dp.message_handler(content_types=ContentTypes.LOCATION)
async def get_full_location(message: Message):
    address = await get_full_address(latitude=message.location.latitude, longitude=message.location.longitude)
    await message.answer(text=address)


@dp.message_handler(text=["Change language", "Tilni o'zgartirish", "Изменить язык"])
async def change_language_handler(message: Message):
    text = "🇺🇿 Tilni tanlang\n 🇬🇧 Select Language\n 🇷🇺 Выберите язык"
    await message.answer(text=text, reply_markup=languages)

@dp.message_handler(text=["🇷🇺 Russian", "🇺🇿 Uzbek", "🇬🇧 English"])
async def change_language_handler_user(message: Message):
    text = _("Til o'zgartirildi")
    await message.answer(text=text, reply_markup=await users_menu_keyboard())