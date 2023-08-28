from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Exists, OuterRef
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Blog
from config.settings import DEFAULT_SECTION
from mailing.forms import ClientForm, MessageForm, MailingSettingForm
from mailing.models import Client, Message, MailingSetting, MailingClinet, MailingLog
from services import is_manager_mailing
from services.cache_services import get_cache_blog


# Create your views here.
class LoginAndActiveRequiredMixin(LoginRequiredMixin):
    """Запрещает неавторизванным и неактивным польователям доступ к view"""

    redirect_field_name = 'redirect_to'


    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_login_url(self):
        if not self.extra_context.get('section'):
            section = DEFAULT_SECTION
        else:
            section = self.extra_context.get('section')
        return reverse_lazy('users:login', kwargs={'section': section})

class ManagerMailingRestrictionMixin(UserPassesTestMixin):
    """ Запрещает пользователям группы manager_mailing доступ к view"""
    def test_func(self):
        user = self.request.user
        # return not self.request.user.groups.filter(name='manager_mailing').exists() and self.request.user.is_active
        return not is_manager_mailing(user) and user.is_active

    def handle_no_permission(self):
        return HttpResponseForbidden()

# Client
class ClientListView(LoginAndActiveRequiredMixin, ListView):
    model = Client
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if not user.is_superuser and not is_manager_mailing(user):
            # Для обычного пользователя выводим только данные, принадлежащие ему
            queryset = super().get_queryset(*args, **kwargs).filter(owner=user.pk)
        else:
            # Для менеджера рассылки и суперпользователя данные не фильтруем
            queryset = super().get_queryset(*args, **kwargs)
        return queryset


# class ClientCreateView(PermissionRequiredMixin, CreateView):
class ClientCreateView(LoginAndActiveRequiredMixin, CreateView):
    model = Client
    # permission_required = 'mailing.add_client'
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

# class ClientUpdateView(PermissionRequiredMixin, UpdateView):
class ClientUpdateView(LoginAndActiveRequiredMixin, UpdateView):
    model = Client
    permission_required = 'mailing.change_client'
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

class ClientDeleteView(LoginAndActiveRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    permission_required = 'mailing.delete_client'
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }
    success_url = reverse_lazy('mailing:client_list')


# Message
class MessageListView(LoginAndActiveRequiredMixin, ListView):
    model = Message
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }


    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if not user.is_superuser and not is_manager_mailing(user):
            # Для обычного пользователя выводим только данные, принадлежащие ему
            queryset = super().get_queryset(*args, **kwargs).filter(owner=user.pk)
        else:
            # Для менеджера рассылки и суперпользователя данные не фильтруем
            queryset = super().get_queryset(*args, **kwargs)
        return queryset

class MessageCreateView(LoginAndActiveRequiredMixin, ManagerMailingRestrictionMixin, CreateView):
# class MessageCreateView(PermissionRequiredMixin, CreateView):
    model = Message
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }
    # permission_required = 'mailing.add_message'
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

# class MessageUpdateView(PermissionRequiredMixin, UpdateView):
class MessageUpdateView(LoginAndActiveRequiredMixin, ManagerMailingRestrictionMixin, UpdateView):
    model = Message
    # permission_required = 'mailing.change_message'
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

# class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
class MessageDeleteView(LoginAndActiveRequiredMixin, ManagerMailingRestrictionMixin, DeleteView):
    model = Message
    # permission_required = 'mailing.delete_message'
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }
    success_url = reverse_lazy('mailing:message_list')


# MailingSetting
class MailingSettingListView(LoginAndActiveRequiredMixin, ListView):
    model = MailingSetting
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }


    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if not user.is_superuser and not is_manager_mailing(user):
            # Для обычного пользователя выводим только данные, принадлежащие ему
            queryset = super().get_queryset(*args, **kwargs).filter(owner=user.pk)
        else:
            # Для менеджера рассылки и суперпользователя данные не фильтруем
            queryset = super().get_queryset(*args, **kwargs)
        return queryset


# class MailingSettingCreateView(PermissionRequiredMixin, CreateView):
class MailingSettingCreateView(LoginAndActiveRequiredMixin, ManagerMailingRestrictionMixin, CreateView):
    model = MailingSetting
    # permission_required = 'mailing.add_mailingsetting'
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:setting_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class MailingSettingUpdateView(LoginAndActiveRequiredMixin, ManagerMailingRestrictionMixin, UpdateView):
    model = MailingSetting
    permission_required = 'mailing.change_mailingsetting'
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:setting_list')

class MailingSettingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MailingSetting
    permission_required = 'mailing.delete_mailingsetting'
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }
    success_url = reverse_lazy('mailing:setting_list')

# MailingClient


class MailingClientListView(LoginRequiredMixin, TemplateView):
    model = MailingClinet
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }
    template_name = 'mailing/mailingclient_list.html'


    def get_context_data(self, *args, **kwargs):
        # print(kwargs.get('pk_setting'))
        context_data = super().get_context_data(*args, **kwargs)
        # print(kwargs.get('pk_setting'))
        pk_setting = self.kwargs.get('pk_setting')
        context_data['pk_setting'] = pk_setting
        context_data['mailingsetting'] = MailingSetting.objects.get(pk=pk_setting)
        context_data['message'] = Message.objects.distinct().filter(mailingsetting__pk=pk_setting)
        context_data['selected_clients_list'] = Client.objects.distinct().filter(mailingclinet__mailing=pk_setting)
        context_data['clients_for_select'] = Client.objects.filter(
                ~Exists(MailingClinet.objects.filter(client=OuterRef('pk'), mailing=pk_setting))
            )

        return context_data

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            pk_setting = request.POST.get('pk_setting')
            pk_clients_list_add = request.POST.getlist('selected_clients')
            pk_clients_list_delete = request.POST.getlist('available_clients')

            for pk_client in pk_clients_list_delete:
                if not MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting):
                    MailingClinet.objects.create(client_id=pk_client, mailing_id=pk_setting)

            for pk_client in pk_clients_list_add:
                if MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting):
                    MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting).delete()

        return redirect(to = reverse_lazy('mailing:mailing_client', args=[pk_setting]))


class ChangeSettingStatusView(PermissionRequiredMixin, UpdateView):
    model = MailingSetting
    form_class = MailingSettingForm
    template_name = 'mailing/setting_confirm_change_status.html'
    permission_required = 'mailing.set_status'
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }
    success_url = reverse_lazy('mailing:setting_list')


    def post(self, request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponseRedirect(self.get_success_url())
        # setting =MailingSetting.objects.get(pk=self.request.POST.get('pk'))
        setting =MailingSetting.objects.get(pk=self.kwargs.get('pk'))
        setting.status = setting.STATUS_FINISHED if setting.status == setting.STATUS_ACTIVATED else setting.STATUS_ACTIVATED  # Инвертируем значение поля status
        setting.save()
        return HttpResponseRedirect(reverse("mailing:setting_list"))


class HomeMailingView(LoginAndActiveRequiredMixin, TemplateView):

    extra_context = {
        'section': 'mailing',
        'title': 'Рассылки',
    }

    template_name = 'mailing/home_mailing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # количество рассылок всего
        context['cnt_mailing_all'] = MailingSetting.objects.all().count()
        # количество активных рассылок
        context['cnt_mailing_active'] = MailingSetting.objects.filter(status=MailingSetting.STATUS_ACTIVATED).count()
        # количество уникальных киентов для рассылок
        context['cnt_clients'] = MailingClinet.objects.values('client_id').distinct().count()


        # 3 случайные статьи из блога
        # blogs_rec = Blog.objects.all()
        blogs_rec = get_cache_blog()
        blogs = list(blogs_rec)
        # Количество случайных записей из блога
        cnt_rand_records = 3
        cnt_records_blogs = len(blogs)
        selected_blogs = []
        for iter in range(cnt_rand_records):
            ind = randint(0,cnt_records_blogs-1)
            selected_blogs.append(blogs.pop(ind))
            cnt_records_blogs-=1

        context['blogs_rand'] = selected_blogs

        return context


class MailingLogListView(PermissionRequiredMixin, ListView):
    model = MailingLog
    extra_context = {
        'section': 'mailing',
        'title': 'Журнал рассылки',
    }
    permission_required = 'mailing.view_mailinglog'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['statuses'] = MailingLog.STATUSES
        return context

    def get_queryset(self, *args, **kwargs):
        status=self.kwargs.get('status')
        if status:
            return MailingLog.objects.filter(status=status)
        else:
            return super().get_queryset(*args, **kwargs)





