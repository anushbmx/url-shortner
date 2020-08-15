from django.contrib import admin

from .models import Shortner


class ShortnerAdmin(admin.ModelAdmin):
	list_display = ['id', 'short_url', 'original_url', 'created']

admin.site.register(Shortner, ShortnerAdmin)