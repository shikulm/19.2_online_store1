from django import forms

from catalog.forms import StyleFormMixtin
from mailing.models import Client, Message, MailingSetting, MailingLog


class ClientForm(StyleFormMixtin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'first_name', 'last_name', 'comment')


class MessageForm(StyleFormMixtin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body')


class MailingSettingForm(StyleFormMixtin, forms.ModelForm):
    class Meta:
        model = MailingSetting
        fields = ('time', 'period', 'status', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['time'].widget.attrs['initial'] = '12:00'

# class MailiingClient(forms):
#     selected_clients =