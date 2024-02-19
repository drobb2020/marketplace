# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Conversation, ConversationMessage


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('item', 'created_at', 'modified_at')
    list_filter = ('item', 'created_at', 'modified_at')
    raw_id_fields = ('members',)
    date_hierarchy = 'created_at'


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'created_at',
        'created_by',
    )
    list_filter = ('conversation', 'created_at', 'created_by')
    date_hierarchy = 'created_at'
