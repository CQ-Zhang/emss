from django.db import transaction
from django.shortcuts import render,HttpResponse,redirect
from emsapp.models import *

# Create your views here.


def login(request):
    name = request.COOKIES.get('name')
    pwd = request.COOKIES.get('pwd')
    if name and pwd:
        name = name.encode('latin-1').decode('utf-8')
        pwd = pwd.encode('latin-1').decode('utf-8')
        result = User.objects.filter(name=name, pwd=pwd)
        print(result)
        if result:
            request.session['login'] = True
            return redirect('home')
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def loginlogic(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    rem = request.POST.get('rem')
    result = User.objects.filter(name=name, pwd=pwd)
    if result:
        r = redirect('home')
        if rem:
            name = name.encode('utf-8').decode('latin-1')
            r.set_cookie('name', name, max_age=7*24*60*600)
            r.set_cookie('pwd', pwd, max_age=7*24*60*600)
        request.session['login'] = True
        return r
    return HttpResponse('登录失败')


def registerlogic(request):
    name = request.POST.get('username')
    pwd = request.POST.get('pwd')
    # print(name, pwd)
    try:
        with transaction.atomic():
            result = User.objects.create(name=name, pwd=pwd)
            if result:
                # 10/0
                return redirect('login')
    except:
        return HttpResponse('注册失败')


def home(request):
    s = request.session.get('login')
    # print(s)
    if s:
        emps = Emp.objects.all()
        return render(request, 'emp.html', {'emp': emps})
    return redirect('login')