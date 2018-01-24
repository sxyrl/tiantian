#coding:utf8
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from models import *
from hashlib import sha1
# Create your views here.

#注册
def register(request):
    context = {'title': '注册'}
    return render(request, 'df_user/register.html', context)

#处理注册请求
def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断两次密码
    if upwd != upwd2:
        return redirect('/user/register/')
    #创建对象
    user = UserInfo()
    user.uname = uname
    #密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #注册成功,转到登录页面
    return redirect('/user/login/')



#验证注册账号是否存在
def register_exist(request):
    uname = request.GET['username']
    print uname
    unames = UserInfo.objects.filter(uname=uname).count()
    return HttpResponse(unames)


#登录

def login(request):
    uname = request.COOKIES.get('uname','')
    print 'login页面的uname是：',uname
    context = {'title': '登录', 'username': uname}
    return render(request, 'df_user/login.html', context)


#处理登录请求
def login_handler(request):
    uname = request.POST.get('username')
    mark = request.POST.get('mark', 0)
    res = HttpResponseRedirect('/user/info/')
    user = UserInfo.objects.filter(uname=uname)
    if mark == '1':
        res.set_cookie('uname', uname)
    else:
        res.set_cookie('uname', '', max_age=-1)
    request.session['user_id'] = user[0].id
    request.session['user_name'] = uname
    return res


#处理登录验证请求
def login_exist(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    s1 = sha1()
    s1.update(upwd)
    upwds = s1.hexdigest()
    user = UserInfo.objects.filter(uname=uname)
    if len(user) == 1 and upwds == user[0].upwd:
        return HttpResponse('1')
    else:
        return HttpResponse('0')

#个人信息
def info(request):
    email = UserInfo.objects.get(id=request.session['user_id']).uemail
    context = {
        'users': request.session['user_name'],
        'email': email,
        'title': '个人中心',
    }
    return render(request, 'df_user/user_center_info.html', context)

#全部订单
def order(request):
    context = {'title': '个人中心'}
    return render(request, 'df_user/user_center_order.html',context)

#收货地址
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        user.ushou = request.POST.get('ushou')
        user.uaddress = request.POST.get('uaddress')
        user.uyoubian = request.POST.get('uyoubian')
        user.uphone = request.POST.get('uphone')
        user.save()
    context = {
        'title': '个人中心',
        'user': user,
    }
    return render(request, 'df_user/user_center_site.html', context)