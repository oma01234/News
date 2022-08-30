from django import template
from django.contrib.auth.models import Group
# 1 no idea what these imports do
# 2 okay so what this file does is that like creates permissions that can be used in the templates

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
