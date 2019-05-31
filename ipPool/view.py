from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def Login(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)

def Index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def Welcome(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'welcome.html', context)

def admin_add(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'admin_add.html', context)
def admin_cate(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'admin_cate.html', context)
def admin_edit(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'admin_edit.html', context)
def admin_list(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'admin_list.html', context)
def admin_role(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'admin_role.html', context)
def admin_rule(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'admin_rule.html', context)


def cate(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'cate.html', context)
def city(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'city.html', context)

def echart1(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts1.html', context)
def echart2(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts2.html', context)
def echart3(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts3.html', context)
def echart4(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts4.html', context)
def echart5(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts5.html', context)
def echart6(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts6.html', context)
def echart7(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts7.html', context)
def echart8(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'echarts8.html', context)



def member_add(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'member_add.html', context)
def member_del(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'member_del.html', context)
def member_edit(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'member_edit.html', context)
def member_list(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'member_list.html', context)
def member_password(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'member_password.html', context)


def order_add(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'order_add.html', context)
def order_list(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'order_list.html', context)
def role_add(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'role_add.html', context)
def unicode(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'unicode.html', context)
def ipMain(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'ipMain.html', context)
