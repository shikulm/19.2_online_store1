import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, FormView

from django.contrib import messages

from config.settings import DEFAULT_SECTION
from users.forms import UserForm, UserRegisterForm, RestorePasswordForm
from users.models import User


# Create your views here.

def logout_redirect_url_app(section):
    if not section:
        section = DEFAULT_SECTION
    return reverse_lazy('mailing:client_list' if section == 'mailing' else 'catalog:home')

def login_redirect_url_app(section):
    if not section:
        section = DEFAULT_SECTION
    return reverse_lazy('mailing:client_list' if section == 'mailing' else 'catalog:home')

def login_url_app(section):
    if not section:
        section = DEFAULT_SECTION
    return reverse_lazy('users:login', args=[section])


def redirect_for_user(section):
    # LOGOUT_REDIRECT_URL = '/'
    # LOGIN_REDIRECT_URL = '/'  # reverse_lazy('catalog:catalog')
    # LOGIN_URL = 'users:login'  # Сюда перенаправляется неавторизованный пользователь

    LOGOUT_REDIRECT_URL = reverse('mailing:client_list') if section == 'mailing' else reverse('catalog:home')
    LOGIN_REDIRECT_URL = reverse('mailing:client_list') if section == 'mailing' else reverse('catalog:home')  # reverse_lazy('catalog:catalog')
    LOGIN_URL = reverse('users:login', args=[section])  # Сюда перенаправляется неавторизованный пользователь


class LoginView(BaseLoginView):
    # Авторизация
    template_name = 'users/login.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if not self.kwargs.get('section'):
            context['section'] = DEFAULT_SECTION
        else:
            context['section'] = self.kwargs.get('section')
        # redirect_for_user(context['section'])
        return context

    def get_success_url(self):
        section = self.get_context_data().get('section')
        # rev = reverse('mailing:client_list') if section == 'mailing' else reverse('catalog:home')
        rev = login_redirect_url_app(section)
        return rev


class LogoutView(LoginRequiredMixin, BaseLogoutView):
# class LogoutView(BaseLogoutView):
    # login_url = reverse('users:login', kwargs={'section': sel})
    redirect_field_name = 'redirect_to'
    # Выход
    # pass
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if not self.kwargs.get('section'):
            context['section'] = DEFAULT_SECTION
        else:
            context['section'] = self.kwargs.get('section')
        # LOGOUT_REDIRECT_URL = reverse('users:login', kwargs={'section': context['section']})
        # redirect_for_user(context['section'])
        # self.next_page = reverse_lazy('users:login', kwargs={'section': context['section']})
        # self.login_url = reverse_lazy('users:login', kwargs={'section': context['section']})
        self.login_url = login_url_app(context['section'])
        return context

    # Переопределение метода get_login_url()
    def get_login_url(self):
        if not self.kwargs.get('section'):
            section = DEFAULT_SECTION
        else:
            section = self.kwargs.get('section')
        # return reverse_lazy('users:login', kwargs={'section': section})
        return reverse_lazy('users:login', kwargs={'section': section})


    def get_success_url(self):
        section = self.get_context_data().get('section')
        print("section = ", section)
        # rev = reverse('mailing:client_list') if section == 'mailing' else reverse('catalog:home')
        rev = logout_redirect_url_app(section)
        return rev

    # def get_logout_redirect_url(self):
    #     if not self.kwargs.get('section'):
    #         section = DEFAULT_SECTION
    #     else:
    #         section = self.kwargs.get('section')
    #     return logout_redirect_url_app(section)
        # return reverse_lazy('mailing:client_list' if section == 'mailing' else 'catalog:home')

    # def dispatch(self, request, *args, **kwargs):
    #     section = self.get_context_data().get('section')
    #     # self.next_page = request.build_absolute_uri(reverse('users:login', kwargs={'section': section}))
    #     self.next_page = request.build_absolute_uri(reverse('users:login', args=(section,)))
    #     return super().dispatch(request, *args, **kwargs)

        # section = self.get_context_data().get('section')
        # # print(section)
        # self.next_page = reverse('users:login', kwargs={'section': section})
        # return super().dispatch(request, *args, **kwargs)

    # def get_success_url(self):
    #     section = self.get_context_data().get('section')
    #     # print(section)
    #     return redirect(reverse('users:login', kwargs={'section': section}))

class RegisterView(CreateView):
    # Регистрация
    model = User
    form_class = UserRegisterForm
    # success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def get_success_url(self):
        section = self.get_context_data().get('section')
        # return redirect(reverse('users:login'), kwargs={'section': section})
        return login_url_app(section)


    def form_valid(self, form):
        # Отправка письма для верификации
        self.object = form.save()
        key_val = random.randint(1, 2147483647)
        self.object.key = key_val
        self.object.save()
        section = self.get_context_data().get('section')
        # print(self.request.POST)
        # link_url = self.request.build_absolute_uri(reverse_lazy('users:verification', kwargs = {'pk' : self.object.pk, 'key':key_val}))
        link_url = self.request.build_absolute_uri(reverse_lazy('users:verification', kwargs = {'pk' : self.object.pk, 'key':key_val, 'section':section}))
        send_mail(
            subject='Регистрация на сайте для покупки шоколада',
            message=f'Поздравляю с регистрацией! \n Для подтверждения пройдите по ссылке {link_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )

        return super().form_valid(form)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if not self.kwargs.get('section'):
            context['section'] = DEFAULT_SECTION
        else:
            context['section'] = self.kwargs.get('section')
        # redirect_for_user(context['section'])
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    # Редактирование профиля
    model = User
    # success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_success_url(self):
        section = self.get_context_data().get('section')
        return reverse('users:profile', kwargs={'section': section})

    def get_object(self, queryset=None, *args, **kwargs):
        # Получаем ссылку на текущего пользователя для редактирования
        return self.request.user


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print('context = ', context)
        # print("до kwargs.get('section') = ", self.kwargs.get('section'))
        # print("до args = ", self.args)
        if not self.kwargs.get('section'):
            context['section'] = DEFAULT_SECTION
        else:
            context['section'] = self.kwargs.get('section')
        # print("после context['section'] = ", context['section'])
        # redirect_for_user(context['section'])
        return context



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
    # success_url = reverse_lazy('users:login')
    form_class = RestorePasswordForm
    def form_valid(self, form):
        if form.is_valid():
            # self.object = form.save()
            email = form.data.get('UserEmail')
            # users = User.objects.filter(email=email)
            users = User.objects.filter(email=email)

            if users:
                self.object = users[0]
                #  Генерируем и сохраняем пароль
                new_pass = User.objects.make_random_password(length=12)
                self.object.set_password(new_pass)
                self.object.save(update_fields=['password'])

                # Отправляем информацию на почту

                section = self.get_context_data().get('section')

                # link_url = self.request.build_absolute_uri(reverse_lazy('users:login'))
                link_url = self.request.build_absolute_uri(reverse_lazy('users:login', kwargs={'section': section}))
                send_mail(
                    subject='Восстановление пароля',
                    message=f'Логин для входа {email}! \n Пароль: {new_pass} \n {link_url}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )

        return super().form_valid(form)



    def get_success_url(self):
        section = self.get_context_data().get('section')
        return reverse('users:login', kwargs={'section': section})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if not self.kwargs.get('section'):
            context['section'] = DEFAULT_SECTION
        else:
            context['section'] = self.kwargs.get('section')
        # redirect_for_user(context['section'])
        return context


# @login_required
def VerificationView(request, pk, key, section):
    # Верификация

    user = User.objects.filter(pk=pk, key=key)[0]
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
        # 'res_verify_msg': res_verify_msg,
        'section': section
        # 'section': DEFAULT_SECTION
    }


    return render(request, 'users/verification.html', context)

