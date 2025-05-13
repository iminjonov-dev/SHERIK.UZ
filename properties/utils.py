from googletrans import Translator

translator = Translator()

def translate_text(text, src_lang, dest_lang):
    """
    Matnni berilgan tildan boshqa tilga tarjima qilish.
    :param text: Tarjima qilinadigan matn
    :param src_lang: Asl til (misol: 'uz', 'ru', 'en')
    :param dest_lang: Maqsadli til
    :return: Tarjima qilingan matn
    """
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Tarjima xatosi: {e}"
