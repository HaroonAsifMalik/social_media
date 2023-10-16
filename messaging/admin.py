from django.contrib import admin
from .models import Message , Conversation

# Register your models here.

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    filter_horizontal = ('participants',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'timestamp', 'is_read')
    list_filter = ('is_read',)


admin.site.register(Message , MessageAdmin)
admin.site.register(Conversation , ConversationAdmin)