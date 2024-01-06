from modeltranslation.translator import TranslationOptions, register
from .models import Profiller

@register(Profiller)
class ProfillerTranslationOptions(TranslationOptions):
    fields = ['Maglumat', 'Salgy', 'Profiliň_ady']
