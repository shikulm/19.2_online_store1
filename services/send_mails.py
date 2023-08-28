import datetime
from smtplib import SMTPException

from django.core.mail import send_mail
from django.conf import settings

from config.settings import get_env_value
from mailing.models import Client, MailingLog, MailingSetting

def send_email(setting: MailingSetting, client: Client):
    '''Отправка письма на почту с созранением результата в журнал'''
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


# def set_status_settings():
#     pass

def send_mails():
    '''Отправляет письмо всем пользоватлеям, подключенным к актуальным рассылкам'''
    # print('Сработал crontab')
    # Изменяем стаусы рассылок с учетом текущего периода
    # set_status_settings()
    # Получаем список активных рассылок
    dt_now = datetime.datetime.now(datetime.timezone.utc)
    # Выбираем настройки, попадающие в период рассылки
    mail_settings = MailingSetting.objects.filter(status=MailingSetting.STATUS_ACTIVATED, datestart__lte=dt_now, dateend__gte=dt_now)
    if mail_settings.exists():
        for ms in mail_settings:
            print('---')
            print('mail_settings: ', ms.message, ms)
            # Определяем сколько дней должно пройти после последний отправки писем, чтобы можно было опять отправлять письма
            days_min = 1 if ms.period == ms.PERIOD_DAILY else 7 if ms.period == ms.PERIOD_WEEKLY else 30
            print(f'После предыдущей рассылки должно пройти миниум {days_min} дней')
            print('---')
            for c in Client.objects.filter(mailingclinet__mailing=ms):
                print("client: ", c)
                # Вычисляем дату последней отправки письма клиенту
                last_log = MailingLog.objects.filter(setting=ms.pk, client_id=c.pk).order_by('-datetime_mailing').first()
                if last_log:

                    date_last = last_log.datetime_mailing
                else:
                    print('раньше не отправляли письма клиенту...')
                    # Если раньще рассылок не было клиенту, то заносим в дату последней рассылки ту дату, с которой рассылка будет выполняться
                    date_last = dt_now-datetime.timedelta(days=(days_min+1))
                print(f'Дата предудщей рассылки: {date_last}. Прошло {dt_now-date_last} из {days_min} дней')
                if (dt_now-date_last) >= datetime.timedelta(days=days_min):
                    print('Отправляем')
                    send_email(ms, c)
                else:
                    print('Прошло мало времени')
    else:
        print('Доступных рассылок нет!')

