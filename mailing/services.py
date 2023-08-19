from smtplib import SMTPException

from django.core.mail import send_mail
from django.conf import settings

from config.settings import get_env_value
from mailing.models import Client, MailingLog, MailingSetting

def send_email(setting: MailingSetting, client: Client):
    '''тправка письма на почту с созранением результата в журнал'''
    res = 0
    res_txt = 'OK'
    try:
        res = send_mail(
            subject = setting.message.subject,
            message = setting.message.body,
            from_email = get_env_value('EMAIL_HOST_USER'),
            recipient_list=[client.email],
            fail_silently=False
        )
    except SMTPException as e:
        res_txt = e

    MailingLog.objects.create(client_id=client.pk, setting_id=setting.pk,
                              status=MailingLog.STATUS_OK if res else MailingLog.STATUS_FAIL,
                              answer=res_txt)


def set_status_settings():
    pass

def send_mails():
    '''Отправляет письмо всем пользоватлеям, подключенным к актуальным рассылкам'''
    # print('Сработал crontab')
    # Изменяем стаусы рассылок с учетом текущего периода
    set_status_settings()
    # Получаем список активных рассылок
    mail_settings = MailingSetting.objects.filter(status=MailingSetting.STATUS_ACTIVATED)
    for ms in mail_settings:
        # print(ms.mailingclinet_set.cl)
        print('mail_settings: ', ms.message, ms )
        print('---')
        for c in Client.objects.filter(mailingclinet__mailing=ms):
            print("client: ", c)
            send_email(ms, c)
