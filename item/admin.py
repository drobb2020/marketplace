# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'id')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'is_sold',
        'created_by',
    )
    list_filter = (
        'category',
        'is_sold',
        'created_by',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
