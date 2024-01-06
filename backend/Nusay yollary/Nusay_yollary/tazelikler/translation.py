from modeltranslation.translator import TranslationOptions, register
from .models import tazelikler

@register(tazelikler)
class tazelikleerTranslationOptions(TranslationOptions):
    fields = ['Tazeligiň_ady', 'Tazeligiň_maglumaty']
