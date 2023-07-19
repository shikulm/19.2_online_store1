from django import template

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
