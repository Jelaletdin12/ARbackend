from django.contrib import admin
from .models import tazelikler
from modeltranslation.admin import TranslationAdmin

class tazeliklerAdmin(TranslationAdmin):
   list_display = ['Tazeligiň_ady']

admin.site.register(tazelikler, tazeliklerAdmin)
