from django.contrib import admin
from .models import GameProduct, UserProfile

# Register your models here.
admin.site.register(GameProduct)
admin.site.register(UserProfile)


class GamesDisplayAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'selling_price'
        'category'
    ]