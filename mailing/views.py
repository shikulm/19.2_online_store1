from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Exists, OuterRef
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.forms import ClientForm, MessageForm, MailingSettingForm
from mailing.models import Client, Message, MailingSetting, MailingClinet


# Create your views here.
# Client
class ClientListView(ListView):
    model = Client
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }

class ClientCreateView(PermissionRequiredMixin, CreateView):
    model = Client
    permission_required = 'mailing.add_client'
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    model = Client
    permission_required = 'mailing.change_client'
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    permission_required = 'mailing.delete_client'
    extra_context = {
        'section': 'mailing',
        'title': 'Клиенты',
    }
    success_url = reverse_lazy('mailing:client_list')


# Message
class MessageListView(ListView):
    model = Message
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }

class MessageCreateView(PermissionRequiredMixin, CreateView):
    model = Message
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }
    permission_required = 'mailing.add_message'
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

class MessageUpdateView(PermissionRequiredMixin, UpdateView):
    model = Message
    permission_required = 'mailing.change_message'
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Message
    permission_required = 'mailing.delete_message'
    extra_context = {
        'section': 'mailing',
        'title': 'Сообщения',
    }
    success_url = reverse_lazy('mailing:message_list')


# MailingSetting
class MailingSettingListView(ListView):
    model = MailingSetting
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }

class MailingSettingCreateView(PermissionRequiredMixin, CreateView):
    model = MailingSetting
    permission_required = 'mailing.add_mailingsetting'
    extra_context = {
        'section': 'mailing',
        'title': 'Настройки',
    }
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:setting_list')

class MailingSettingUpdateView(PermissionRequiredMixin, UpdateView):
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




# class MailingClientListView(ListView):
class MailingClientListView(TemplateView):
# class MailingClientListView(View):
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
        # context_data['clint_for_select'] = Client.Objects.filter(mailingsetting__pk=context_data['pk'], mailingclinent__)
        context_data['selected_clients_list'] = Client.objects.distinct().filter(mailingclinet__mailing=pk_setting)
        print("context_data['selected_clients_list'] = ", context_data['selected_clients_list'])
        context_data['clients_for_select'] = Client.objects.filter(
                ~Exists(MailingClinet.objects.filter(client=OuterRef('pk'), mailing=pk_setting))
            )
        print("context_data['clients_for_select'] = ", context_data['clients_for_select'])

        return context_data

    def post(self, request, *args, **kwargs):
        print('MailingClientListView.POST')
        print(self.request.method)
        if request.method == 'POST':
            # pk_setting = self.kwargs['pk_setting']
            pk_setting = request.POST.get('pk_setting')
            print('pk_setting ', pk_setting)
            pk_clients_list_add = request.POST.getlist('selected_clients')
            print('pk_clients_list_add', pk_clients_list_add)
            pk_clients_list_delete = request.POST.getlist('available_clients')
            print('pk_clients_list_delete', pk_clients_list_delete)


            for pk_client in pk_clients_list_delete:
                if not MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting):
                    MailingClinet.objects.create(client_id=pk_client, mailing_id=pk_setting)

            for pk_client in pk_clients_list_add:
                if MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting):
                    MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting).delete()

        # return render(request, 'mailing/mailingsetting_list.html')
        # return render(request, 'mailing/mailingclient_list.html', pk_setting)
        return redirect(to = reverse_lazy('mailing:mailing_client', args=[pk_setting]))
        # return render(request, 'mailing/mailingclient_list.html', 1)


# def post(self, request, *args, **kwargs):
    #     if self.request.method == 'POST':
    #         # pk_setting = self.request.POST['pk_setting']
    #         pk_setting = self.kwargs.get('pk_setting')
    #         print('pk_setting=', pk_setting)
    #         pk_clients_list_add = request.POST.getlist('selected-clients')
    #         print('pk_clients_list_add', pk_clients_list_add)
    #         pk_clients_list_delete = request.POST.getlist('available-clients')
    #         print('pk_clients_list_delete', pk_clients_list_delete)
    #         for pk_client in pk_clients_list_add:
    #             print('pk_client=', pk_client)
    #             # MailingClinet.objects.create(client_id=pk_client, mailing_id=pk_setting)
    #     # return super().post(request, *args, **kwargs)
    #     return render(request, reverse_lazy('mailing:mailing_client'), args=[pk_setting])
    #     # return redirect(reverse(viewname='mailing:mailing_client', args=[pk_setting]))

    # def post(self):
    # return redirect(reverse(viewname='mailing:mailing_client', args=[pk_setting]))

# def toggle_clients(request, *args, **kwargs):
#     print('toggle_clients')
#     print(request.method)
#     if request.method == 'POST':
#         # pk_setting = self.kwargs['pk_setting']
#         pk_setting = request.POST['pk_setting']
#         form = request.POST['form']
#         print("form ", form.attrs)
#         pk_clients_list_delete = request.POST.getlist('selected-clients')
#         pk_clients_list_add = request.POST.getlist('available-clients')
#         print('pk_clients_list_add ', pk_clients_list_add)
#         print('pk_clients_list_delete ', pk_clients_list_delete)
#
#         for pk_client in pk_clients_list_add:
#             if not MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting):
#                 MailingClinet.objects.create(client_id=pk_client, mailing_id=pk_setting)
#
#         for pk_client in pk_clients_list_delete:
#             if MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting):
#                 MailingClinet.objects.filter(client_id=pk_client, mailing_id=pk_setting).delete()
#
#     # return render(request, 'mailing/mailingclient_list.html', pk_setting)
#     return redirect(to = 'mailing/mailingclient_list.html', args= [pk_setting])

# def toggle_clients(request, *args, **kwargs):
#     clients_for_select = MailingClinet.objects.all()
#     object_list = []
#     pk_setting=kwargs.get('pk_setting')
#
#     if request.method == 'POST':
#         object_list_ids = request.POST.getlist('selected_clients')
#         object_list = MailingClinet.objects.filter(client_id__in=object_list_ids, mailing_id=pk_setting)
#         print(object_list_ids)
#         # context = request.POST.get('context')
#
#
#         # Сохранение выбранных элементов в модели
#
#         # context = {
#         #     'object_list': object_list,
#         #     'clients_for_select': clients_for_select,
#         #     'pk_setting': pk_setting,
#         # }
#         return HttpResponse('Success')
#
#         # return redirect(reverse(viewname='mailing:mailing_client', args=[pk_setting]))
#     # return render(request, reverse('mailing:mailing_client', kwargs={'pk_setting': pk_setting,}), context)
#     return render(request, 'mailing/mailingclient_list.html')

# def toggle_clients_add(request, pk_setting):
#     '''Добавление выбранных клиентов в список рассылки'''
#     print('Вызван контроллер toggle_clients_add()')
#     print(f'request.method {request.method}')
#     print("request.POST = ", request.POST)
#     print("request.GET = ", request.GET)
#     if request.method == 'POST':
#         pk_clients_list = request.POST.getlist('available-items')
#         print('pk_clients_list = ', pk_clients_list)
#         print('pk_client_ish = ', request.POST['available-items'])
#         # pk_setting = request.POST['pk_setting']
#         for pk_client in pk_clients_list:
#             print('pk_client=', pk_client)
#             MailingClinet.objects.create(client_id=pk_client, mailing_id=pk_setting)
#
#     return redirect(reverse(viewname='mailing:mailing_client', args=[pk_setting]))