def is_manager_mailing(user):
    return user.groups.filter(name__icontains='manager_mailing').exists()