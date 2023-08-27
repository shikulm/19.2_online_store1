__all__ = [
    'send_mails',
    'is_manager_mailing',
]

from services.send_mails import send_mails
from services.users_services import is_manager_mailing