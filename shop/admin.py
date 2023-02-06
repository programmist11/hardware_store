from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Cart, Category


class CartAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('id', "title", 'descriptions', "category", 'price', 'photo')
    list_display_links = ('id', "title", 'descriptions', "category", 'price', 'photo')
    list_filter = ('category', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "title")
    list_display_links = ('id', "title")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart, CartAdmin)
