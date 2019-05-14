from django.shortcuts import render

# Create your views here.
#coding=utf-8
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from tools import generate_code
from django.views import View 
from django.contrib import auth
from . import models
import random, datetime, os, string
from cacheout import Cache
import copy

cache = Cache()

input_lists = {
    'crystal_list': {
        'density': '密度(kg/m3)',
        'literature': '文献',
        'temperature': '温度(k)',
        'volume': '体积(Å3/atom)',
        'brittle_tough': '脆韧性',
        'chem_formula': '化学式',
        'structure_Id': '结构ID',
        'space_group': '空间群',
        'alloy_grade': '合金牌号',
        'info_source': '信息来源',
        'mater_cate': '材料类别',
        'energy': '能量(eV)',
        'latt_cons': '晶格常数(Å)',
        'main_elem': '主元素及含量',
        'second_elem': '次元素及含量',
        'trace_elem': '微量元素及含量',
        'rerong': '热容(J/molK)',
        'rpzxs': '热膨胀系数(/K)',
        'atomic_ener': '单位原子能(eV)',
        'form_ener': '单位原子形成能(eV/atom)',
        'elastic_cons': '单晶弹性常数(Gpa)',
        'wPoisson_rate': '微观泊松比(无量纲)',
        'elasti_anis': '微观弹性各异性(Gpa)',
        'wG_Ress': '微观切变模量(Gpa)',
        'wK_Ress': '微观体积模量(Gpa)'
    }
}

def del_session(request):
    try:
        del request.session['username']
        del request.session['permission']
    except KeyError:
        pass

def check_login(cookie_name, per_type='3', func_type='func'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if func_type == 'class':
                req = args[1]
            else:
                req = args[0]

            if req.session.get('username') is None or \
            req.session.get('permission') is None:
                del_session(req)
                return redirect('/dbms/login/')
            if int(per_type) < int(req.session.get('permission')):
                print('No permission!')
                return redirect('/dbms/mainterface/')
            # if (func_type == 'class' and args[1].session.get('username') is None) or \
            # (func_type == 'func' and args[0].session.get('username') is None):
            #     return redirect('/dbms/login/')
            # if ((func_type == 'class' and (args[1].session.get('permission') is None or int(per_type) < int(args[1].session.get('permission')))) or \
            # (func_type == 'func' and (args[0].session.get('permission') is None or int(per_type) < int(args[0].session.get('permission'))))):
            #     return redirect('/dbms/mainterface/')
            res = func(*args, **kwargs)
            if cookie_name != '':
                res.set_cookie('current_page', cookie_name)
            return res
        return wrapper
    return decorator

def to_mainterface(func_type='func'):
    def decorator(func):
        def wrapper(*args):
            print(args)
            if (func_type == 'class' and args[1].session.get('username')) or \
            (func_type == 'func' and args[0].session.get('username')):
                return redirect('/dbms/mainterface/')
            return func(*args)
        return wrapper
    return decorator

class Login(View):
    VERIFY_IMG_DIR = os.path.dirname(os.path.dirname(__file__)) + '/static/verify_code'

    def add_verify():
        global cache
        today_str = datetime.date.today().strftime("%Y%m%d")
        verify_path = "%s/%s" % (Login.VERIFY_IMG_DIR, today_str)
        if not os.path.isdir(verify_path):
            os.makedirs(verify_path, exist_ok=True)
        #print("session:",request.session.session_key)
        random_filename = "".join(random.sample(string.ascii_lowercase,4))
        random_code = generate_code.gene_code(verify_path,random_filename)
        cache.set(random_filename, random_code, ttl=30)
        return {"filename":random_filename, "today_str":today_str, 'error': ''}

    @to_mainterface('class')
    def post(self, request):
        global cache
        _verify_code = request.POST.get('verify_code')
        _verify_code_key  = request.POST.get('verify_code_key')
        print(cache.get(_verify_code_key))
        print(_verify_code)
        if cache.get(_verify_code_key) is not None and cache.get(_verify_code_key).lower() == _verify_code.lower():
            u = request.POST.get('username')
            p = request.POST.get('password')
            check = models.UserInfo.objects.filter(username=u, password=p).first()
            if check:
                request.session['username'] = u
                request.session['permission'] = check.permission
                return redirect('/dbms/mainterface/', {'iframeurl': 'http://39.106.148.96/dbms/maingraph/'})
                # response = redirect('/dbms/mainterface/')
                # response.set_cookie('username', u)
                # return response
            else:
                error_msg = "用户名或密码错误!"
        else:
            error_msg = "验证码错误!"

        return_dict = Login.add_verify()
        print('!!!' + str(cache.get(_verify_code_key)))
        return_dict['error'] = error_msg

        return render(request, 'login.html', return_dict)

    @to_mainterface('class')
    def get(self, request):
        return_dict = Login.add_verify()

        return render(request, 'login.html', return_dict)

@check_login('')
def mainterface(request):
    print(request.COOKIES)
    if request.COOKIES.get('current_page') is not None:
        iframeurl = 'http://39.106.148.96/dbms/%s/' % request.COOKIES.get('current_page')
    else:
        iframeurl = 'http://39.106.148.96/dbms/maingraph/'
    if request.session.get("permission") == '1':
        return render(request, 'mainterface_admin.html', {'iframeurl': iframeurl})
    elif request.session.get("permission") == '2':
        return render(request, 'mainterface_user.html', {'iframeurl': iframeurl})
    elif request.session.get("permission") == '3':
        return render(request, 'mainterface_reader.html', {'iframeurl': iframeurl})
    else:
        return redirect('/dbms/login/')

def logout(request):
    auth.logout(request)
    del_session(request)
    res = redirect('/dbms/login/')
    res.delete_cookie('current_page')
    return res
    # response = redirect('/dbms/login/')
    # response.delete_cookie('username')
    # return response

@check_login('maingraph')
def main_graph(request):
    print(request.path)
    return render(request, 'maingraph.html')

@check_login('crystalselect')
def crystal_select(request):
    return render(request, 'crystalselect.html')

@check_login('crystalinsert', 2)
def crystal_insert(request):
    if request.method == 'GET':
        return render(request, 'crystalinsert.html')
    else:
        input_dic = {}
        ret_dic = {}
        for attr in input_lists['crystal_list'].keys():
            content = request.POST.get(attr).strip()
            if content is not None and content != '':
                input_dic[attr] = content

        if (input_dic.get('main_elem') is not None \
        and input_dic.get('second_elem') is not None) \
        or input_dic.get('alloy_grade') is not None:
            models.Djbasicnatu.objects.create(**input_dic)
            ret_dic['success'] = '添加成功'
        else:
            ret_dic['error'] = '合金牌号或主元素与次元素必须填写'
        return render(request, 'crystalinsert.html', ret_dic)

@check_login('crystalquery')
def crystal_query(request):
    if request.method == 'GET':
        return render(request, 'crystalquery.html')
    else:
        select_fields = set()
        select_conditions = {}
        for k, v in request.POST.items():
            if k == 'select':
                continue
            if k[-1] == '1':
                if v.strip() != '':
                    select_fields.add(k[0:-1])
                    if k == 'second_elem1':
                        select_conditions['second_elem__icontains'] = '%'.join(v.strip().split(' '))
                        print(models.Djbasicnatu.objects.filter(second_elem__icontains=select_conditions['second_elem__icontains']).values('id'))
                    else:
                        select_conditions[k[0:-1] + '__icontains'] = v.strip()
            else:
                select_fields.add(k)

        if len(select_fields) == 0:
            return render(request, 'crystalquery.html')
        select_result = models.Djbasicnatu.objects.filter(**select_conditions).values(*select_fields)
        field_names = [input_lists['crystal_list'][name] for name in select_fields]
        result = [[columns[field] for field in select_fields] for columns in select_result]
        
        return render(request, 'crystalquery.html', {'fields': field_names, 'result': result})

@check_login('processselect')
def process_select(request):
    return render(request, 'processselect.html')

@check_login('processinsert', 2)
def process_insert(request):
    return render(request, 'processinsert.html')

@check_login('testselect')
def test_select(request):
    return render(request, 'testselect.html')

@check_login('testinsert', 2)
def test_insert(request):
    return render(request, 'testinsert.html')

@check_login('', 2)
def first(request, p1, p2):
    res = render(request, 'first%d-%d.html' % (p1, p2))
    res.set_cookie('current_page', 'first%d-%d' % (p1, p2))
    return res

@check_login('usermanage', 1)
def user_manage(request):
    if request.method == 'GET':
        select_users = models.UserInfo.objects.all()
    else:
        select_users = models.UserInfo.objects.filter(username__icontains=request.POST.get('usersearch'))
    users = [{'name': user.username, 'permission': user.permission} for user in select_users]
    print(type(users))
    return render(request, 'usermanage.html', {'users': users})

@check_login('adduser', 1)
def add_user(request):
    if request.method == 'GET':
        return render(request, 'adduser.html')
    else:
        ret_dic = {}
        u = request.POST.get('username')
        p = request.POST.get('password')
        per = request.POST.get('permission')
        if models.UserInfo.objects.filter(username=u).first():
            ret_dic['user_error'] = '用户名已存在'
        if len(p) < 3:
            ret_dic['password_error'] = '密码太短'
        if len(ret_dic) == 0:
            ret_dic['success'] = '添加成功'
            user_insert = models.UserInfo()
            user_insert.username = u
            user_insert.password = p
            user_insert.permission = per
            user_insert.save()
            return render(request, 'adduser.html', ret_dic)
        else:
            return render(request, 'adduser.html', ret_dic)


@check_login('usermanage', 1)
def del_user(request, username):
    models.UserInfo.objects.filter(username=username).delete()
    return user_manage(request)


# cache = Cache()
# VERIFY_IMG_DIR = os.path.dirname(os.path.dirname(__file__)) + '/static/verify_code'

# def login(request):
#     error_msg = ''
#     today_str = datetime.date.today().strftime("%Y%m%d")
#     verify_path = "%s/%s" % (VERIFY_IMG_DIR, today_str)
#     if not os.path.isdir(verify_path):
#         os.makedirs(verify_path, exist_ok=True)
#     print("session:",request.session.session_key)
#     random_filename = "".join(random.sample(string.ascii_lowercase,4))
#     random_code = generate_code.gene_code(verify_path,random_filename)
#     cache.set(random_filename, random_code, ttl=30)

#     if request.method == 'POST':

#         _verify_code = request.POST.get('verify_code')
#         _verify_code_key  = request.POST.get('verify_code_key')
#         print(cache.get(_verify_code_key))
#         print(_verify_code)
#         if cache.get(_verify_code_key) is not None and cache.get(_verify_code_key).lower() == _verify_code.lower():
#             print("code verification pass!")
#         else:
#             error_msg = "验证码错误!"

#     return render(request,'login.html',{"filename":random_filename, "today_str":today_str, "error":error_msg})




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
