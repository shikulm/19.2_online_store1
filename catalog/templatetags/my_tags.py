from django import template

from services import is_manager_mailing

register = template.Library()


# Создание фильтра
@register.filter
def mediapath(val):
    if val:
        return f"/media/{val}"
    # return "/static/catalog/default_shoc.jpg"
    return "/static/catalog/default_shoc.png"
    # return "{% static 'catalog/default_shoc.jpg' %}"


# Создание тега
@register.simple_tag
def mediapath_tag(val):
    if val:
        return f"/media/{val}"
    return "/static/catalog/default_shoc.jpg"
    # return "/static/catalog/default_shoc.png"

@register.filter
def get_type(value):
    return type(value).lower()

@register.simple_tag(takes_context=True)
def check_group(context, group_name):
    # Проверяет включение пользователя в группу
    user = context['user']
    return user.groups.filter(name=group_name).exists()


@register.simple_tag(takes_context=True)
def is_manager_mailing_tag(context):
    # Проверяет входит ли пользователь в группу manager_mailing
    user = context['user']
    is_manager_mailing_tag = user.groups.filter(name='manager_mailing').exists()
    print("user = ", user)
    print("user.groups.filter(name='manager_mailing').exists() = ", user.groups.filter(name='manager_mailing').exists())
    # Добавляем результат в контекст шаблона

    context['is_manager_mailing'] = is_manager_mailing_tag
    # return is_manager_mailing(user)
    # return user.groups.filter(name='manager_mailing').exists()
    return is_manager_mailing(user)
    # return {'is_manager_mailing': is_manager_mailing(user)}
    # return user

@register.filter
def get_to_len(val, len_to=100):
    # Делает строку длиной len_to
    if val:
        try:
            # return (len_to+" ")[:len_to]
            s = val+' '*len_to
            return s[:len_to+1]
        except TypeError:
            return val
    return ''
