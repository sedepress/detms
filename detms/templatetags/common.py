from django import template
from tms.models import Project
from django.http import JsonResponse

register = template.Library()

@register.simple_tag
def get_projects():
    projects = list(Project.objects.all().values())
    return JsonResponse({'code': 0, 'data': projects})