from django.shortcuts import render

# Create your views here.
#coding=utf-8
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from tools import generate_code, generate_graph
from django.views import View 
from django.contrib import auth
from . import models
from django.forms.models import model_to_dict
import random, datetime, os, string
from cacheout import Cache
from django.utils.safestring import SafeString
from pytz import timezone
from .forms import UploadFileForm
import json
import time

cache = Cache()

input_lists = {
    'literature_list': {
        'serial_num': ('文献编号', 'char'),
        'p_name': ('文献名称', 'char'),
        'author': ('作者', 'char'),
        'point_word': ('主要内容', 'char'),
        'open_book': ('发表期刊', 'char'),
        'open_time': ('发表时间', 'date'),
    },
    'crystal_list': {
        'density': ('密度(kg/m3)', 'float'),
        'literature': ('文献', 'char'),
        'temperature': ('温度(k)', 'float'),
        'volume': ('体积(Å3/atom)', 'char'),
        'brittle_tough': ('脆韧性', 'char'),
        'chem_formula': ('化学式', 'char'),
        'structure_Id': ('结构ID', 'char'),
        'space_group': ('空间群', 'float'),
        'alloy_grade': ('合金牌号', 'char'),
        'info_source': ('信息来源', 'char'),
        'mater_cate': ('材料类别', 'char'),
        'energy': ('能量(eV)', 'float'),
        'latt_cons': ('晶格常数(Å)', 'char'),
        'main_elem': ('主元素及含量', 'char'),
        'second_elem': ('次元素及含量', 'char'),
        'trace_elem': ('微量元素及含量', 'char'),
        'rerong': ('热容(J/molK)', 'float'),
        'rpzxs': ('热膨胀系数(/K)', 'float'),
        'atomic_ener': ('单位原子能(eV)', 'float'),
        'form_ener': ('单位原子形成能(eV/atom)', 'char'),
        'elastic_cons': ('单晶弹性常数(Gpa)', 'char'),
        'wPoisson_rate': ('微观泊松比(无量纲)', 'float'),
        'elasti_anis': ('微观弹性各异性(Gpa)', 'float'),
        'wG_Ress': ('微观切变模量(Gpa)', 'int'),
        'wK_Ress': ('微观体积模量(Gpa)', 'int')
    },
    'process_list': {
        'literature': ('文献', 'char'),
        'info_source': ('信息来源', 'char'),
        'chem_formula': ('化学式', 'char'),
        'alloy_grade': ('合金牌号', 'char'),
        'main_elem': ('主元素及含量', 'char'),
        'second_elem': ('次元素及含量', 'char'),
        'trace_elem': ('微量元素及含量', 'char'),
        'smelting_voltage': ('熔炼电压(V)', 'float'),
        'qProcessing_sample': ('加工前试样', 'char'),
        'process_tech': ('加工工艺', 'char'),
        'qSample_size': ('加工前试样尺寸', 'char'),
        'qsyx_com': ('加工前试样组成', 'char'),
        'heat_temp': ('加热温度(℃)', 'float'),
        'qsyjld': ('加工前试样晶粒度(μm)', 'char'),
        'qsyzg': ('加工前试样织构', 'char'),
        'smelting_vacuum': ('熔炼真空度(Pa)', 'float'),
        'smelting_current': ('熔炼电流(kA)', 'float'),
        'smelting_times': ('熔炼次数(次)', 'float'),
        'ingot_diameter': ('铸锭直径(mm)', 'float'),
        'nominal_ability': ('公称能力(MN)', 'float'),
        'extruder_tonnage': ('挤压机吨位(t)', 'float'),
        'jyt_diameter': ('挤压筒直径(mm)', 'float'),
        'jy_heattemp': ('挤压加热温度(℃)', 'float'),
        'jy_bwtime': ('挤压保温时间(min)', 'float'),
        'bw_time': ('保温时间(min)', 'float'),
        'yz_jjrtime': ('轧制加热温度(℃)', 'float'),
        'yz_bwtime': ('轧制保温时间(min)', 'float'),
        'dc_maxprorate': ('道次最大加工率(%)', 'float'),
        'all_prorate': ('总加工率(%)', 'float'),
        'quenching_medium': ('淬火介质()', 'char'),
        'quenching_temp': ('淬火温度(℃)', 'float'),
        'hProcessing_sample': ('加工后试样', 'char'),
        'annealing_type': ('退火种类', 'char'),
        'annealing_temp': ('退火温度(℃)', 'float'),
        'annealing_time': ('退火时间(min)', 'float'),
        'hSample_size': ('加工后试样尺寸', 'char'),
        'hsyx_com': ('加工后试样组成', 'char'),
        'hsyjld': ('加工后试样晶粒度', 'char'),
        'hsyzg': ('加工后试样织构', 'char')
    },
    'test_list': {
        'literature': ('文献', 'char'),
        'info_source': ('信息来源', 'char'),
        'chem_formula': ('化学式', 'char'),
        'alloy_grade': ('合金牌号', 'char'),
        'main_elem': ('主元素及含量', 'char'),
        'second_elem': ('次元素及含量', 'char'),
        'trace_elem': ('微量元素及含量', 'char'),
        'hProcess_sample': ('加工后试样', 'char'),
        'hSample_size': ('试样尺寸', 'char'),
        'hsyx_com': ('试样组成', 'char'),
        'hsyjld': ('试样晶粒度(μm)', 'char'),
        'hsyzg': ('试样织构', 'char'),
        'xntest_cond': ('性能测试条件', 'char'),
        'xntest_temp': ('性能测试温度(k)', 'float'),
        'xndeform_rate': ('性能测试速率', 'char'),
        'hPoisson_rate': ('泊松比', 'float'),
        'coercivity': ('矫顽力(G)', 'float'),
        'work_fun': ('功函数(V)', 'float'),
        'bulk_modulu': ('体模量(Pa)', 'float'),
        'magnetic_rate': ('磁导率(H/m)', 'float'),
        'conductivity': ('电导率(S/m)', 'float'),
        'shear_modulus': ('剪切模量(Pa)', 'float'),
        'curie_temp': ('居里温度(℃)', 'float'),
        'young_modulus': ('杨氏模量(Pa)', 'float'),
        'heat_rate': ('热导率(W/m·k)', 'float'),
        'bheat_capa': ('比热容(J/kg·K)', 'float'),
        'tensile_strength': ('抗拉强度(MPa)', 'float'),
        'yield_strength': ('屈服强度(MPa)', 'float'),
        'breaking_strength': ('断裂强度(MPa)', 'float'),
        'dhys_rate': ('断后延伸速率(%)', 'float'),
        'rswell_modu': ('热膨胀系数(1/℃)', 'float'),
        'rfs_rate': ('热辐射率(W/m2)', 'float'),
        'dielectric_con': ('介电常数(C2/N·m2)', 'float'),
        'bhmagnetic_str': ('饱和磁感应强度(A/m)', 'float')
    },
    'radiation_list': {
        'literature': ('文献', 'char'),
        'info_source': ('信息来源', 'char'),
        'chem_formula': ('化学式', 'char'),
        'alloy_grade': ('合金牌号', 'char'),
        'main_elem': ('主元素及含量', 'char'),
        'second_elem': ('次元素及含量', 'char'),
        'trace_elem': ('微量元素及含量', 'char'),
        'Neu_num': ('快中子注量', 'float'),
        'hProcess_sample': ('辐射前试样', 'char'),
        'Irr_cond': ('辐射条件名称', 'char'),
        'hsyx_com': ('辐射前试样尺寸', 'char'),
        'Ray_type': ('射线类型', 'char'),
        'hsyjld': ('辐射前试样晶粒度(μm)', 'char'),
        'hsyzg': ('辐射前试样织构', 'char'),
        'Ray_stro': ('射线强度', 'float'),
        'Irr_time': ('辐照时间', 'float'),
        'hSample_size': ('辐射前试样尺寸', 'char'),
        'Hirr_sycc': ('辐射后试样尺寸', 'char'),
        'Hirr_symc': ('辐射后试样名称', 'char'),
        'Hirr_syjld': ('辐射后试样晶粒度', 'char'),
        'Hirr_syzg': ('辐射后试样织构', 'char')
    }
}

def get_table_ch(table):
    if table == 'crystal':
        return '晶体'
    elif table == 'process':
        return '加工'
    elif table == 'test':
        return '测试'
    elif table == 'radiation':
        return '辐射'
    elif table == 'literature':
        return '文献'
    elif table == 'picture':
        return '图像'
    else:
        return ''

def get_model(table):
    if table == 'crystal':
        return models.Djbasicnatu
    elif table == 'process':
        return models.Process_table
    elif table == 'test':
        return models.Test_table
    elif table == 'radiation':
        return models.Radiation_table
    elif table == 'literature':
        return models.Literature
    elif table == 'picture':
        return models.Picture
    else:
        return None

def check_type(input_info, content, ret_dic):
    if input_info[1] == 'float':
        try:
            return float(content)
        except ValueError:
            ret_dic['errors'].append('%s应该为浮点型\n' % input_info[0])
            return ''
    elif input_info[1] == 'int':
        try:
            return int(content)
        except ValueError:
            ret_dic['errors'].append('%s应该为整型\n' % input_info[0])
            return ''
    elif input_info[1] == 'date':
        try:
            if '-' in content:
                t = time.strptime(content, '%Y-%m-%d')
            elif '/' in content:
                t = time.strptime(content, '%Y/%m/%d')
            else:
                t = time.strptime(content, '%Y %m %d')
            return time.strftime('%Y-%m-%d', t)
        except:
            ret_dic['errors'].append('%s应该为以\'-\'或\'/\'或空格分割的时间类型\n' % input_info[0])
            return ''

    return content

def del_session(request):
    try:
        for k in request.session.keys():
            del request.session[k]
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
            if cookie_name != '' and 'query' not in cookie_name:
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
    res.delete_cookie('select_fields')
    res.delete_cookie('select_conditions')
    res.delete_cookie('save_para')
    return res
    # response = redirect('/dbms/login/')
    # response.delete_cookie('username')
    # return response

@check_login('maingraph')
def main_graph(request):
    print(request.path)
    return render(request, 'maingraph.html')

def check_input(list_type, input_dic, ret_dic):
    if list_type == 'literature':
        if input_dic.get('serial_num') is None \
        or input_dic.get('p_name') is None:
            ret_dic['errors'].append('文献编号与文献名称必须填写')
    elif list_type == 'picture':
        pass
    else:
        if (input_dic.get('main_elem') is None \
        or input_dic.get('second_elem') is None) \
        and input_dic.get('alloy_grade') is None:
            ret_dic['errors'].append('合金牌号或主元素与次元素必须填写')

def all_insert(request, table):
    if request.method == 'GET':
        return render(request, table + 'insert.html')
    else:
        input_dic = {}
        ret_dic = {'errors': []}
        print(request.POST)
        for attr in input_lists[table + '_list'].keys():
            content = request.POST.get(attr).strip()
            if content is not None and content != '':
                if attr == 'literature':
                    l = models.Literature.objects.filter(serial_num=content).first()
                    if l:
                        input_dic[attr] = l
                    else:
                        ret_dic['errors'].append('文献编号在数据库中未查询到')
                else:
                    input_dic[attr] = check_type(input_lists[table + '_list'][attr], content, ret_dic)

        check_input(table, input_dic, ret_dic)
        if len(ret_dic['errors']) == 0:
            get_model(table).objects.create(**input_dic)
            ret_dic['success'] = '添加成功'

        return render(request, table + 'insert.html', ret_dic)

'''
默认为0，如果是奇数，添加图像
如果是3代表没有update
'''
def all_query(request, table, upde = 0):
    if request.session['permission'] == '3':
        update_on = False
        delete_on = False
    else:
        if upde // 2 == 1:
            update_on = False
        else:
            update_on = True
        delete_on = True
    if upde % 2 == 1:
        pic_on = True
    else:
        pic_on = False

    if request.method == 'GET':
        try:
            select_fields = set(json.loads(request.COOKIES.get('select_fields')).get(table, '').split(','))
            select_conditions = json.loads(request.COOKIES.get('select_conditions')).get(table, {})
        except json.decoder.JSONDecodeError:
            select_fields = []
            select_conditions = {}
        select_fields.add('id')
        select_fields.add('insert_time')
        if len(select_fields) == 0:
            return render(request, 'query.html', {'update_on': update_on, 'delete_on': delete_on, 'pic_on': pic_on})

        select_result = get_model(table).objects.filter(**select_conditions).order_by('-insert_time').values(*select_fields)
        for s in select_result:
            for k, v in s.items():
                print(k, v)
        select_fields.remove('id')
        select_fields.remove('insert_time')
        field_names = [input_lists[table + '_list'][name][0] for name in select_fields]
        result = [{'id': columns['id'], 'time': columns['insert_time'],'value': [columns[field] for field in select_fields]} for columns in select_result]

        res = render(request, 'querylow.html', {'update_on': update_on, 'delete_on': delete_on, 'pic_on': pic_on, 'name_ch': get_table_ch(table), 'querytype': table, 'fields': field_names, 'result': result})
        return res
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
                        select_conditions['second_elem__icontains'] = '[%]'.join(v.strip().split(' '))
                        print(select_conditions['second_elem__icontains'])
                    else:
                        select_conditions[k[0:-1] + '__icontains'] = v.strip()
            else:
                select_fields.add(k)

        if len(select_fields) == 0:
            if request.session['permission'] == '3':
                return render(request, 'querylow.html')
            else:
                return render(request, 'queryhigh.html')
        select_fields.add('insert_time')
        select_fields.add('id')
        select_result = get_model(table).objects.filter(**select_conditions).order_by('-insert_time').values(*select_fields)
        select_fields.remove('id')
        select_fields.remove('insert_time')
        field_names = [input_lists[table + '_list'][name][0] for name in select_fields]
        result = [{'id': columns['id'], 'time': columns['insert_time'], 'value': [columns[field] for field in select_fields]} for columns in select_result]
        
        res = render(request, 'querylow.html', {'update_on': update_on, 'delete_on': delete_on, 'pic_on': pic_on, 'name_ch': get_table_ch(table), 'querytype': table, 'fields': field_names, 'result': result})
        sf = request.COOKIES.get('select_fields')
        if sf is not None:
            sf_map = json.loads(sf)
        else:
            sf_map = {}
        sf_map[table] = ','.join(list(select_fields))
        res.set_cookie('select_fields', json.dumps(sf_map))
        sc = request.COOKIES.get('select_conditions')
        if sc is not None:
            sc_map = json.loads(sc)
        else:
            sc_map = {}
        sc_map[table] = select_conditions
        res.set_cookie('select_conditions', json.dumps(sc_map))
        return res

def all_delete(request, id, table):
    get_model(table).objects.filter(id=id).delete()
    return redirect('/dbms/' + table + 'query')

def all_update(request, id, table):
    if request.method == 'GET':
        result = model_to_dict(get_model(table).objects.filter(id=id).first())
        for (k, v) in result.items():
            if v is None:
                result[k] = ''

        return render(request, table + 'update.html', {'result': result})
    else:
        input_dic = {}
        ret_dic = {'errors': []}
        for attr in input_lists[table + '_list'].keys():
            if attr == 'insert_time':
                continue
            content = request.POST.get(attr).strip()
            if content is not None and content != '':
                input_dic[attr] = check_type(input_lists[table + '_list'][attr], content, ret_dic)

        check_input(table, input_dic, ret_dic)
        if len(ret_dic['errors']) == 0:
            get_model(table).objects.filter(id=id).update(**input_dic)
            return redirect('/dbms/' + table + 'query')
        else:
            result = model_to_dict(get_model(table).objects.filter(id=id).first())
            for (k, v) in result.items():
                if v is None:
                    result[k] = ''
            ret_dic['result'] = result
            return render(request, table + 'update.html', ret_dic)

def all_allin(request, table):
    if request.method == 'POST':
        file_type = request.POST.get('filetype')
        if file_type is None:
            return render(request, table + 'insert.html', {'all_error': '请选择上传文件的类型'})
        else:
            file = request.FILES.get('datafile')
            if file is None:
                return render(request, table + 'insert.html', {'all_error': '请选择要上传的文件'})
            #form = UploadFileForm(request.POST, request.FILES)
            all_count = 0
            success_count = 0
            header = []
            last = ''
            error_list = []
            mc = get_model(table)
            for chunk in file.chunks():
                chunk = last + chunk.decode(encoding = "utf-8")
                lines = chunk.split('\n')
                try:
                    last = lines[-1]
                except IndexError:
                    last = ''
                lines = lines[:-1]
                for line in lines:
                    all_count += 1
                    if file_type == 'json':
                        try:
                            input_dic = json.loads(line)
                            mc.objects.create(**input_dic)
                            success_count += 1
                        except TypeError:
                            error_list.append('line %d' % all_count + line)
                        except ValueError:
                            error_list.append('line %d' % all_count + line)
                    else:
                        if len(header) == 0:
                            header = line.split(',')
                            all_count -= 1
                        else:
                            input_dic = {}
                            input_list = line.split(',')
                            ret_dic = {'errors': []}
                            if len(input_list) > 0:
                                for i in range(len(input_list)):
                                    input_dic[header[i]] = check_type(input_lists[table + '_list'][header[i]], input_list[i], ret_dic)
                                if len(ret_dic['errors']) == 0:
                                    mc.objects.create(**input_dic)
                                    success_count += 1
                                else:
                                    error_list.append('line %d' % all_count + line)

            if last != '':
                all_count += 1
                if file_type == 'json':
                    try:
                        input_dic = json.loads(last)
                        mc.objects.create(**input_dic)
                        success_count += 1
                    except TypeError:
                        error_list.append('line %d' % all_count + last)
                    except ValueError:
                        error_list.append('line %d' % all_count + last)
                else:
                    input_dic = {}
                    input_list = last.split(',')
                    ret_dic = {'errors': []}
                    for i in range(len(input_list)):
                        input_dic[header[i]] = check_type(input_lists[table + '_list'][header[i]], input_list[i], ret_dic)
                    if len(ret_dic['errors']) == 0:
                        mc.objects.create(**input_dic)
                        success_count += 1
                    else:
                        error_list.append('line %d' % all_count + last)
            return render(request, table + 'insert.html', {'all_success': '已成功插入%d/%d条数据，失败数据如下：' % (success_count, all_count), 'all_errors': error_list})

def all_allout(request, table):
    if request.method == 'POST':
        try:
            select_fields = set(json.loads(request.COOKIES.get('select_fields')).get(table, '').split(','))
            select_conditions = json.loads(request.COOKIES.get('select_conditions')).get(table, {})
        except json.decoder.JSONDecodeError:
            select_fields = []
            select_conditions = {}
        select_fields.add('id')
        select_fields.add('insert_time')
        if len(select_fields) == 0:
            if request.session['permission'] == '3':
                return render(request, 'querylow.html')
            else:
                return render(request, 'queryhigh.html')

        select_result = get_model(table).objects.filter(**select_conditions).order_by('-insert_time').values(*select_fields)
        res = HttpResponse(content_type='application/octet-stream')
        res.write(','.join(list(select_fields)) + '\n')
        for column in select_result:
            c = [str(column[field]) for field in select_fields]
            res.write(','.join(c) + '\n')
        #res['Content_Type'] = 'application/octet-stream'
        res['Content-Disposition'] = 'attachment;filename="%s.csv"' % table
        return res


@check_login('literatureselect')
def literature_select(request):
    return render(request, 'literatureselect.html')

@check_login('literatureinsert', 2)
def literature_insert(request):
    return all_insert(request, 'literature')

@check_login('literatureselect')
def literature_query(request):
    return all_query(request, 'literature')

@check_login('literatureselect', 2)
def literature_delete(request, id):
    return all_delete(request, id, 'literature')

@check_login('literatureselect', 2)
def literature_update(request, id):
    return all_update(request, id, 'literature')

@check_login('literatureinsert', 2)
def literature_allin(request):
    return all_allin(request, 'literature')

@check_login('literatureselect')
def literature_allout(request):
    return all_allout(request, 'literature')

@check_login('crystalselect')
def crystal_select(request):
    return render(request, 'crystalselect.html')

@check_login('crystalinsert', 2)
def crystal_insert(request):
    return all_insert(request, 'crystal')

@check_login('crystalselect')
def crystal_query(request):
    return all_query(request, 'crystal')

@check_login('crystalselect', 2)
def crystal_delete(request, id):
    return all_delete(request, id, 'crystal')

@check_login('crystalselect', 2)
def crystal_update(request, id):
    return all_update(request, id, 'crystal')

@check_login('crystalinsert', 2)
def crystal_allin(request):
    return all_allin(request, 'crystal')

@check_login('crystalselect')
def crystal_allout(request):
    return all_allout(request, 'crystal')

@check_login('processselect')
def process_select(request):
    return render(request, 'processselect.html')

@check_login('processinsert', 2)
def process_insert(request):
    return all_insert(request, 'process')

@check_login('processselect')
def process_query(request):
    return all_query(request, 'process', 1)

@check_login('processselect', 2)
def process_delete(request, id):
    return all_delete(request, id, 'process')

@check_login('processselect', 2)
def process_update(request, id):
    return all_update(request, id, 'process')

@check_login('processinsert', 2)
def process_allin(request):
    return all_allin(request, 'process')

@check_login('processselect')
def process_allout(request):
    return all_allout(request, 'process')

@check_login('testselect')
def test_select(request):
    return render(request, 'testselect.html')

@check_login('testinsert', 2)
def test_insert(request):
    return all_insert(request, 'test')

@check_login('testselect')
def test_query(request):
    return all_query(request, 'test', 1)

@check_login('testselect', 2)
def test_delete(request, id):
    return all_delete(request, id, 'test')

@check_login('testselect', 2)
def test_update(request, id):
    return all_update(request, id, 'test')

@check_login('testinsert', 2)
def test_allin(request):
    return all_allin(request, 'test')

@check_login('testselect')
def test_allout(request):
    return all_allout(request, 'test')

@check_login('radiationselect')
def radiation_select(request):
    return render(request, 'radiationselect.html')

@check_login('radiationinsert', 2)
def radiation_insert(request):
    return all_insert(request, 'radiation')

@check_login('radiationselect')
def radiation_query(request):
    return all_query(request, 'radiation', 1)

@check_login('radiationselect', 2)
def radiation_delete(request, id):
    return all_delete(request, id, 'radiation')

@check_login('radiationselect', 2)
def radiation_update(request, id):
    return all_update(request, id, 'radiation')

@check_login('radiationinsert', 2)
def radiation_allin(request):
    return all_allin(request, 'radiation')

@check_login('radiationselect')
def radiation_allout(request):
    return all_allout(request, 'radiation')

@check_login('pictureselect')
def picture_select(request):
    return render(request, 'pictureselect.html')

@check_login('pictureselect')
def picture_query(request):
    return all_query(request, 'picture', 3)

@check_login('pictureselect', 2)
def picture_delete(request, id):
    return all_delete(request, id, 'picture')

@check_login('', 2)
def first(request, p1, p2):
    print(dict(request.POST))
    if request.method == 'GET':
        para = request.COOKIES.get('save_para', '{}')
        print(json.loads(para))
        res = render(request, 'first%d-%d.html' % (p1, p2), {'save_para': json.loads(para)})
        res.set_cookie('current_page', 'first%d-%d' % (p1, p2))
        return res
    elif request.POST.get('save') is not None:
        save_para = json.loads(request.COOKIES.get('save_para', '{}'))
        for k, v in dict(request.POST).items():
            if k != 'save' and k != 'reset':
                save_para[k] = v

        para = json.dumps(save_para)
        res = render(request, 'first%d-%d.html' % (p1, p2), {'save_para': save_para, 'success': '保存成功'})
        res.set_cookie('current_page', 'first%d-%d' % (p1, p2))
        res.set_cookie('save_para', para)
        return res
    else:
        save_para = json.loads(request.COOKIES.get('save_para', '{}'))
        for k, _ in request.POST.items():
            if k in save_para:
                save_para.pop(k)

        res = render(request, 'first%d-%d.html' % (p1, p2), {'save_para': {}, 'success': '重置成功'})
        res.set_cookie('current_page', 'first%d-%d' % (p1, p2))
        res.set_cookie('save_para', json.dumps(save_para))
        return res

def compute_return(para):
    path = None
    if para.get('cllb') is not None:
        current_str = datetime.datetime.now(timezone('Asia/Shanghai')).strftime("%Y%m%d%H%M%S")
        if not os.path.isdir('graph_result'):
            os.makedirs('graph_result', exist_ok=True)
        path = 'graph_result/' + current_str + '.jpeg'
        generate_graph.gs_graph(None, path)

    return path

@check_login('compute', 2)
def compute(request):
    if request.method == 'GET':
        return render(request, 'compute.html')
    else:
        para = request.COOKIES.get('save_para', '{}')
        path = compute_return(json.loads(para))
        print(path)
        if path:
            with open(path, 'rb') as file:
                file_content = file.read()
            res = HttpResponse(content_type='application/octet-stream')
            res.write(file_content)
            #res['Content_Type'] = 'application/octet-stream'
            res['Content-Disposition'] = 'attachment;filename="compute_graph.jpg"'
            return res
        else:
            return render(request, 'compute.html', {'error': '无法计算，请重新检查上传参数'})


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
