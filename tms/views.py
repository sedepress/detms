from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from tms.forms import LineForm

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
    return render(request, 'tms/line/index.html', {})

@login_required
def line_store(request):
    if request.method == 'POST':
        form = LineForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'code': 200, 'msg': '添加成功！'})
        else:
            print(form.errors)

    return render(request, 'tms/line/store.html', {})