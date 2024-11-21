async def get_lang_by_text(language: str):
    if language == "🇬🇧 English":
        return "en"
    elif language == "🇷🇺 Russian":
        return "ru"
    else:
        return "uz"