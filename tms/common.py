from tms.models import Project
from django.http import JsonResponse

def get_projects(request):
    projects = list(Project.objects.all().values())
    return JsonResponse({'code': 0, 'data': projects})