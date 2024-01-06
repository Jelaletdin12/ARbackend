from django.contrib import admin
from .models import Profiller, ProfileImage
from modeltranslation.admin import TranslationAdmin

class ProfileImageInline(admin.TabularInline):
    model = ProfileImage
    extra = 1




class ProfileAdmin(TranslationAdmin):
    inlines = [ProfileImageInline]
    list_display = ['Profiliň_ady']


admin.site.register(Profiller, ProfileAdmin)
