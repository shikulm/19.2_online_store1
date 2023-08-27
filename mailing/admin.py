from django.contrib import admin

from mailing.models import Client, Message, MailingSetting, MailingClinet, MailingLog


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'owner',)
    list_filter = ('email', 'first_name', 'last_name', 'owner',)
    search_fields = ('period', 'status', 'message', 'owner',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'owner',)
    list_filter = ('subject', 'body', 'owner',)
    search_fields = ('period', 'status', 'message', 'owner',)

@admin.register(MailingSetting)
class MailingSettingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'datestart', 'dateend', 'period', 'status', 'message', 'owner',)
    list_filter = ('datestart', 'dateend', 'period', 'status', 'message', 'owner',)
    search_fields = ('period', 'status', 'message', 'owner',)


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