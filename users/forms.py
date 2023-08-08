from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleFormMixtin
from users.models import User


class UserRegisterForm(StyleFormMixtin, UserCreationForm):
    class Meta:
        model = User
        # fields ="__all__"
        fields =('email', 'password1', 'password2')

class UserForm(StyleFormMixtin, UserChangeForm):
    class Meta:
        model = User
        # fields ="__all__"
        fields =('email', 'password', 'first_name', 'last_name', 'phone','country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class RestorePasswordForm(forms.Form):
    model = User
    UserEmail = forms.EmailField(label='Ваша почта', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['UserEmail'].widget.attrs['class'] = 'form-control'
        self.fields['UserEmail'].widget.attrs['placeholder'] = 'name@email.com'
        # self.UserEmail.widget['class'] = 'form-control'
        # self.UserEmail.widget['placeholder'] = 'name@email.com'
