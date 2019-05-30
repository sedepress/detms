from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, QueryDict
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from tms.forms import LineForm
from tms.models import Line, Project, Customer
import logging

@login_required
def index(request):
    return render(request, 'tms/index.html', {})

@login_required
def welcome(request):
    return render(request, 'tms/welcome.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse('账户未激活！，请联系管理员。')
        else:
            print('Invalid login detail: {0}, {1}'.format(username, password))
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'tms/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def user_list(request):
    return render(request, 'tms/user_list.html', {})

@login_required
def line_index(request):
    lines = Line.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', None)
        if name:
            lines = Line.objects.filter(name__contains=name)

    page_lines = Paginator(lines, 10)
    page = request.GET.get('page', 1)
    data = page_lines.get_page(page)

    return render(request, 'tms/line/index.html', {'data': data})

@login_required
def line_store(request):
    if request.method == 'POST':
        form = LineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            exist_line = Line.objects.filter(name=name)
            if exist_line:
                return JsonResponse({'code': 400, 'msg': '已存在相同线路！'})
            form.save()
            return JsonResponse({'code': 200, 'msg': '新增线路成功！'})
        else:
            logging.info(form.errors)
            return JsonResponse({'code': 400, 'msg': '线路格式不符合规范！'})

    return render(request, 'tms/line/store.html', {})

@login_required
def line_update(request, line_id):
    try:
        line = Line.objects.get(id=line_id)
    except Line.DoesNotExist:
        line = None

    if request.method == 'PATCH':
        put = QueryDict(request.body)
        data = LineForm(put)
        if data.is_valid():
            line.__dict__.update(**data.cleaned_data)
            is_exist_line = Line.objects.filter(name=data.cleaned_data.get('name'))
            if is_exist_line:
                return JsonResponse({'code': 400, 'msg': '已存在相同线路！'})
            line.save()
            return JsonResponse({'code': 200, 'msg': '更新成功！'})


    return render(request, 'tms/line/store.html', {'line': line})

@login_required
def line_delete(request, line_id):
    if request.method == 'DELETE':
        try:
            line = Line.objects.get(id=line_id)
        except Line.DoesNotExist:
            return JsonResponse({'code': 500, 'msg': '系统异常！'})
        line.delete()
        return JsonResponse({'code': 200, 'msg': '删除线路成功！'})

@login_required
def consignment_index(request):
    return render(request, 'tms/consignment/index.html', {})

@login_required
def consignment_store(request):
    if request.method == 'POST':
        form = LineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            exist_line = Line.objects.filter(name=name)
            if exist_line:
                return JsonResponse({'code': 400, 'msg': '已存在相同线路！'})
            form.save()
            return JsonResponse({'code': 200, 'msg': '新增线路成功！'})
        else:
            logging.info(form.errors)
            return JsonResponse({'code': 400, 'msg': '线路格式不符合规范！'})

    projects = Project.objects.all()
    customers = Customer.objects.all()

    return render(request, 'tms/consignment/store.html', {'projects': projects, 'customers': customers})