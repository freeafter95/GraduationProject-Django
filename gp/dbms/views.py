from django.shortcuts import render

# Create your views here.
#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from tools import generate_code
import datetime
import os

VERIFY_IMG_DIR = '/static/verify_code'

def login(request):
    error_msg = {}
    today_str = datetime.date.today().strftime("%Y%m%d")
    verify_path = "%s/%s" % (VERIFY_IMG_DIR, today_str)
    if not os.path.isdir(verify_path):
        os.makedirs(verify_path, exist_ok=True)
    print("session:",request.session.session_key)
    random_filename = "".join(random.sample(string.ascii_lowercase,4))
    random_code = generate_code.gene_code(verify_path,random_filename)
    cache.set(random_filename, random_code,30)

    if request.method == 'POST':

        _verify_code = request.POST.get('verify_code')
        _verify_code_key  = request.POST.get('verify_code_key')
        if cache.get(_verify_code_key) == _verify_code:
            print("code verification pass!")
        else:
            error_msg['error'] = "验证码错误!"

    return render(request,'login.html',{"filename":random_filename, "today_str":today_str, "error":err_msg})




# from django import forms
# from dbms.models import User

# #表单
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名',max_length=100)
#     password = forms.CharField(label='密码',widget=forms.PasswordInput())


#注册
# def regist(req):
#     if req.method == 'POST':
#         uf = UserForm(req.POST)
#         if uf.is_valid():
#             #获得表单数据
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             #添加到数据库
#             User.objects.create(username= username,password=password)
#             return HttpResponse('regist success!!')
#     else:
#         uf = UserForm()
#     return render_to_response('regist.html',{'uf':uf}, )

# #登陆
# def login(req):
#     if req.method == 'POST':
#         uf = UserForm(req.POST)
#         if uf.is_valid():
#             #获取表单用户密码
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             #获取的表单数据与数据库进行比较
#             user = User.objects.filter(username__exact = username,password__exact = password)
#             if user:
#                 #比较成功，跳转index
#                 response = HttpResponseRedirect('/dbms/index/')
#                 #将username写入浏览器cookie,失效时间为3600
#                 response.set_cookie('username',username,3600)
#                 return response
#             else:
#                 #比较失败，还在login
#                 return HttpResponseRedirect('/dbms/login/')
#     else:
#         uf = UserForm()
#     return render_to_response('login.html',{'uf':uf}, )

# def test(req):
#     return render_to_response('test.html', {} )

# #登陆成功
# def index(req):
#     username = req.COOKIES.get('username','')
#     return render_to_response('index.html' ,{'username':username})

# #退出
# def logout(req):
#     response = HttpResponse('logout !!')
#     #清理cookie里保存username
#     response.delete_cookie('username')
#     return response
