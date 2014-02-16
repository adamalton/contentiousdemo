from django.contrib import admin

from contentioussite.models import TextString


class TextStringAdmin(admin.ModelAdmin):
    list_display = ('label', 'text')
    ordering = ('id',)

admin.site.register(TextString, TextStringAdmin)
