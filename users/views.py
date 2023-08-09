import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render


from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, FormView

from django.contrib import messages

from users.forms import UserForm, UserRegisterForm, RestorePasswordForm
from users.models import User


# Create your views here.

class LoginView(BaseLoginView):
    # Авторизация
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, BaseLogoutView):
    # Выход
    pass


class RegisterView(CreateView):
    # Регистрация
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        # Отправка письма для верификации
        self.object = form.save()
        key_val = random.randint(1, 2147483647)
        self.object.key = key_val
        self.object.save()
        # print(self.request.POST)
        link_url = self.request.build_absolute_uri(reverse_lazy('users:verification', kwargs = {'pk' : self.object.pk, 'key':key_val}))
        send_mail(
            subject='Регистрация на сайте для покупки шоколада',
            message=f'Поздравляю с регистрацией! \n Для подтверждения пройдите по ссылке {link_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )

        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    # Редактирование профиля
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        # Получаем ссылку на текущего пользователя для редактирования
        return self.request.user



# def RestorePasswordView(request):
#     """Восстановление пароля"""
#     if request.method == "POST":
#         email = request.POST.get('UserEmail')
#
#         # Генерация пароля


    # return render(request, 'users/login.html', context)


class RestorePasswordView(FormView):
    # Восстановление пароля
    template_name = 'users/restore_password.html'
    success_url = reverse_lazy('users:login')
    form_class = RestorePasswordForm
    def form_valid(self, form):
        if form.is_valid():
            # self.object = form.save()
            email = form.data.get('UserEmail')
            # users = User.objects.filter(email=email)
            users = User.objects.get(email=email)

            if users:
                self.object = users[0]
                #  Генерируем и сохраняем пароль
                new_pass = User.objects.make_random_password(length=12)
                self.object.set_password(new_pass)
                self.object.save(update_fields=['password'])

                # Отправляем информацию на почту
                link_url = self.request.build_absolute_uri(reverse_lazy('users:login'))
                send_mail(
                    subject='Восстановление пароля',
                    message=f'Логин для входа {email}! \n Пароль: {new_pass} \n {link_url}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )

        return super().form_valid(form)


@login_required
def VerificationView(request, pk, key):
    # Верификация

    user = User.objects.filter(pk=pk, key=key)
    if user:
        # Успешная верифкация
        success_verify = True
        # user = user_verify[0]
        # res_verify_msg = 'Поздравляем! \n Ваша почта подтверждена!'

        user.is_active = success_verify
        user.save(update_fields=['is_active'])

        login(request, user)
        messages.add_message(request, messages.INFO, f'Учетная запись {user.email} активирована')
    else:
        # Ошибка верифкация
        success_verify = False
        # res_verify_msg = 'Ошибка верификации. \n Попробуйте еще раз'
        messages.add_message(request, messages.ERROR, f'Ошибка верификации. \n Попробуйте еще раз')
    context = {
        'success_verify': success_verify,
        # 'res_verify_msg': res_verify_msg
    }


    return render(request, 'users/verification.html', context)

