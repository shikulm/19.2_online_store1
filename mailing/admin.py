from django.contrib import admin

from mailing.models import Client, Message, MailingSetting, MailingClinet, MailingLog


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name')
    list_filter = ('email', 'first_name', 'last_name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject')
    list_filter = ('subject', 'body',)

@admin.register(MailingSetting)
class MailingSettingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'period', 'status', 'message')
    list_filter = ('time', 'period', 'status', 'message',)
    search_fields = ('period', 'status', 'message',)


@admin.register(MailingClinet)
class MailingClinetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mailing', 'client')
    list_filter = ('mailing', 'client',)
    search_fields = ('mailing', 'client',)

@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'datetime_mailing', 'client', 'setting', 'status', 'answer')
    list_filter = ('datetime_mailing', 'client', 'setting', 'status', 'answer',)
    search_fields = ('client', 'setting', 'status',)