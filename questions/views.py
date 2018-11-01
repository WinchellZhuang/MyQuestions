from django.shortcuts import render
from questions.models import *
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.paginator import Paginator #分页查询的功能封装
import json

# -----------------------------主框架页面--------------------------------------
def index(request):
    return render(request, 'questions/index.html')

# -----------------------------默认首页--------------------------------------
def first(request):
    return render(request, 'questions/first.html')

# -----------------------------疑问记录页--------------------------------------
def qst_record(request):
    return render(request,'questions/qst_record.html')

# -----------------------------用户管理--------------------------------------
def userManager(request):
    return render(request, 'questions/userManager.html')
def user_save(request):
    # print('接口进入 。。。。。。。')
    u_real_name = request.POST.get('u_real_name')
    u_login_name = request.POST.get('u_login_name')
    u_pwd = request.POST.get('u_pwd')
    # print('*' * 100)
    #print('--->>' + u_real_name + ':' + u_login_name + ':' + u_pwd + '<<---')
    #print(type(u_real_name))
    # print('*'*100)
    user = UserInfo()
    user.u_login_name = u_login_name
    user.u_real_name = u_real_name
    user.u_pwd = u_pwd
    # print(user)
    # user.u_create_datetime =datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        user.save()
        return HttpResponse('ok')
    except Exception as ex:
        return HttpResponse(ex)
def user_list(request):
    # 前台传过来的页码和页容量
    page = request.POST.get('page')
    pagesize = request.POST.get('pagesize')

    userList = UserInfo.objects.all()
    # 创建分页对象，传入要分页的集合和页容量
    p = Paginator(userList,int(pagesize))
    # 通过 p 可取得总记录条数
    pageCount = p.count
    # 通过 P 取得可分页数
    pageSizeCount = p.num_pages
    # 取得要查询页的数据，这才是重点,传入参数页码，如第二页
    userList = p.page(page)

    #方法一： 用model_to_dict方法转换JSON可行，不过我的时间字段没有转换#
    # user_dict_list = []
    # for user in userList:
    #    user_dict_list.append(model_to_dict(user))
    #    print(model_to_dict(user))#
    # return JsonResponse({"Rows":user_dict_list})

    #方法二： 用 __dict__方法  需要手动删除 _state 项
    # user_dict_list = []
    # for user in userList:
    #    dict = {}
    #    dict.update(user.__dict__)
    #    del dict['_state']
    #    user_dict_list.append(dict)
    # return  JsonResponse({"Rows":user_dict_list})

    #方法三： 用serializers将对象序列化成JSON，并取出需要的数据重新封装
    user_dict_list = []
    #序列化成string字符串
    strJson = serializers.serialize('json', userList)
    # 通过 import json的loads方法将字符串转换成list集合对象
    objJson = json.loads(strJson)
    for mo in objJson:
        # 因为序列化时，会将主键单独在fields之外，所以用 arr['id'] = value
        # 这种字典添加修改字典的方法把 id 追加到字典当中
        mo['fields']['id']=mo['pk']
        user_dict_list.append(mo['fields'])
    # 将格式调整成LingerUI表格需要的样式，完成
    return JsonResponse({"Total":p.count,"Rows": user_dict_list})
def user_update(request):
    strJson = request.POST.get('js')
    objJson = json.loads(strJson)
    user = UserInfo.objects.get(id=int(objJson['id']))
    user.u_real_name = objJson['u_real_name']
    user.u_login_name = objJson['u_login_name']
    user.u_pwd = objJson['u_pwd']
    user.save()
    return  HttpResponse('ok')
def user_del(request):
    strJson = request.POST.get('js')
    objJson = json.loads(strJson)
    user = UserInfo.objects.get(id=int(objJson['id']))
    user.delete()
    return HttpResponse("ok")

# -----------------------------疑问科目--------------------------------------
def subjectManager(request):
    return render(request, 'questions/subject.html')
def subject_save(request):
    s_name = request.POST.get('s_name')

    subject =SubjectInfo()
    subject.s_name = s_name
    try:
        subject.save()
        return HttpResponse('ok')
    except Exception as ex:
        return HttpResponse(ex)
def subject_list(request):
    # 前台传过来的页码和页容量
    page = request.POST.get('page')
    pagesize = request.POST.get('pagesize')
    subjectList = SubjectInfo.objects.all()
    p = Paginator(subjectList,int(pagesize))
    pageCount = p.count
    pageSizeCount = p.num_pages
    subjectList = p.page(page)
    print(subjectList)
    subject_dict_list = []
    strJson = serializers.serialize('json', subjectList)
    objJson = json.loads(strJson)
    for mo in objJson:
        mo['fields']['id']=mo['pk']
        subject_dict_list.append(mo['fields'])
    return JsonResponse({"Total":p.count,"Rows": subject_dict_list})
def subject_update(request):
    strJson = request.POST.get('js')
    #print("------------------->>:"+strJson)
    objJson = json.loads(strJson)
    subject = SubjectInfo.objects.get(id=int(objJson['id']))
    subject.s_name = objJson['s_name']
    subject.save()
    return  HttpResponse('ok')
def subject_del(request):
    strJson = request.POST.get('js')
    objJson = json.loads(strJson)
    subject = SubjectInfo.objects.get(id=int(objJson['id']))
    subject.delete()
    return HttpResponse("ok")

# -----------------------------问题来源--------------------------------------
def qstManager(request):
    return render(request, 'questions/qstSource.html')
def qst_save(request):
    q_source = request.POST.get('q_source')
    qst =QuestionSource()
    qst.q_source = q_source
    try:
        qst.save()
        return HttpResponse('ok')
    except Exception as ex:
        return HttpResponse(ex)
def qst_list(request):
    # 前台传过来的页码和页容量
    page = request.POST.get('page')
    pagesize = request.POST.get('pagesize')
    qstList = QuestionSource.objects.all()
    p = Paginator(qstList,int(pagesize))
    pageCount = p.count
    pageSizeCount = p.num_pages
    qstList = p.page(page)
    #print(subjectList)
    qst_dict_list = []
    strJson = serializers.serialize('json', qstList)
    objJson = json.loads(strJson)
    for mo in objJson:
        mo['fields']['id']=mo['pk']
        qst_dict_list.append(mo['fields'])
    return JsonResponse({"Total":p.count,"Rows": qst_dict_list})
def qst_update(request):
    strJson = request.POST.get('js')
    #print("------------------->>:"+strJson)
    objJson = json.loads(strJson)
    qst = SubjectInfo.objects.get(id=int(objJson['id']))
    qst.q_source = objJson['q_source']
    qst.save()
    return  HttpResponse('ok')
def qst_del(request):
    strJson = request.POST.get('js')
    objJson = json.loads(strJson)
    qst = SubjectInfo.objects.get(id=int(objJson['id']))
    qst.delete()
    return HttpResponse("ok")

# -----------------------------解决等级/状态--------------------------------------
def solveLevel(request):
    return render(request, 'questions/solveLevel.html')
def sl_save(request):
    s_solve = request.POST.get('s_solve')
    sl =QuestionSolve()
    sl.s_solve = s_solve
    try:
        sl.save()
        return HttpResponse('ok')
    except Exception as ex:
        return HttpResponse(ex)
def sl_list(request):
    # 前台传过来的页码和页容量
    page = request.POST.get('page')
    pagesize = request.POST.get('pagesize')
    slList = QuestionSolve.objects.all()
    p = Paginator(slList,int(pagesize))
    pageCount = p.count
    pageSizeCount = p.num_pages
    slList = p.page(page)
    #print(subjectList)
    sl_dict_list = []
    strJson = serializers.serialize('json', slList)
    objJson = json.loads(strJson)
    for mo in objJson:
        mo['fields']['id']=mo['pk']
        sl_dict_list.append(mo['fields'])
    return JsonResponse({"Total":p.count,"Rows": sl_dict_list})
def sl_update(request):
    strJson = request.POST.get('js')
    #print("------------------->>:"+strJson)
    objJson = json.loads(strJson)
    sl = QuestionSolve.objects.get(id=int(objJson['id']))
    sl.s_solve = objJson['s_solve']
    sl.save()
    return  HttpResponse('ok')
def sl_del(request):
    strJson = request.POST.get('js')
    objJson = json.loads(strJson)
    sl = QuestionSolvesl.objects.get(id=int(objJson['id']))
    sl.delete()
    return HttpResponse("ok")