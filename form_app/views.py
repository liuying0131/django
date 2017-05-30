# coding:utf-8
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template

from models import User
# Create your views here.
from .form import *


# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密__码', widget=forms.PasswordInput())


def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            # User.objects.get_or_create(username = username,password = password)
            registAdd = User.objects.get_or_create(username=username, password=password)[1]
            if registAdd == False:
                # return HttpResponseRedirect('/share/')
                return render_to_response('share.html', {'registAdd': registAdd, 'username': username})
            else:
                return render_to_response('share.html', {'registAdd': registAdd})

    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 对比提交的数据与数据库中的数据
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/index/')
                usertype = req.POST.get('user_type')
                print 'usertype:' + usertype
                # 将username写入浏览器cookie，失效时间为3600
                response.set_cookie('username', username, 360000)
                response.set_cookie('usertype', usertype, 360000)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))


# 登录成功
def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username': username})


# 退出登录

def logout(req):
    response = HttpResponse('logout!!!')
    # 清除cookie里保存的username
    response.delete_cookie('username')
    return response


def share(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            return render_to_response('share.html', {'username': username})
    else:
        uf = UserForm()
    return render_to_response('share.html', {'uf': uf})


# 添加学生记录
def addstudent(req):

    if req.method == 'POST':
        acaname= req.POST.get("acaname")
        classnum=req.POST.get("classnum")
        stuid=req.POST.get("stuid")
        username=req.POST.get("username")
        sex=req.POST.get("sex")

        Student.objects.get_or_create(acaname=acaname,classnum=classnum,stuid=stuid,username=username,sex=sex)
        return render(req,'base.html')
    return render(req,"addstudent.html")



def viewstudent(req):
    stuid = req.GET.get("stuid")
    delstuid = req.GET.get("del")
#    editstuid = req.GET.get("edit")
    username = req.COOKIES.get('username', '')
    usertype = req.COOKIES.get('usertype')
    if delstuid:  # 如果有delstuid 视作删除,这是 ajax传过来的请求做的处理
        stulist = Student.objects.filter(stuid=delstuid).delete()

    elif stuid:  # 如果有stuid 视做查询,
        stulist = Student.objects.filter(stuid=stuid).order_by('stuid')

    else:
        stulist = Student.objects.all().order_by('stuid')

    return render_to_response("viewstudent.html",
                              context_instance=RequestContext(req, {"stulist": stulist, 'username': username,
                                                                    "usertype": usertype}))


def editstudent(req):
    if req.method=='GET':
        nid=req.GET.get('nid')
        stulist = Student.objects.filter(id=nid)
        return render(req,"editstudent.html", {"stulist": stulist})
    elif req.method == 'POST':
        nid=req.GET.get('nid')
        newacaname= req.POST.get("newacaname")
        newclassnum=req.POST.get("newclassnum")
        newstuid=req.POST.get("newstuid")
        newusername=req.POST.get("newusername")
        newsex=req.POST.get("newsex")
        Student.objects.filter(id=nid).update(acaname=newacaname,classnum=newclassnum,stuid=newstuid,username=newusername,sex=newsex)
        return render(req,"base.html")




def addgrade(req):
    if req.method == 'POST':
        acaname= req.POST.get("acaname")
        stuid=req.POST.get("stuid")
        username=req.POST.get("username")
        grade1=req.POST.get("grade1")
        grade2=req.POST.get("grade2")
        grade3=req.POST.get("grade3")

        Grade.objects.get_or_create(acaname=acaname,stuid=stuid,username=username,grade1=grade1,grade2=grade2,grade3=grade3)
        return render(req,'base.html')
    return render(req,"addgrade.html")


def searchgrade(req):
    stuid = req.GET.get("stuid")
    username = req.COOKIES.get('username', '')

    gradelist = Grade.objects.filter(stuid=stuid).order_by('stuid')
    return render_to_response("searchgrade.html",
                              context_instance=RequestContext(req, {"gradelist": gradelist, 'username': username}))


def editgrade(req):
    stuid = req.GET.get("stuid")
    delstuid = req.GET.get("del")
    alterstuid = req.GET.get("alter")
    username = req.COOKIES.get('username', '')
    usertype = req.COOKIES.get('usertype')
    if delstuid:  # 如果有delstuid 视作删除,这是 ajax传过来的请求做的处理
        gradelist = Grade.objects.filter(stuid=delstuid).delete()
    elif stuid:  # 如果有stuid 视做查询,
        gradelist = Grade.objects.filter(stuid=stuid).order_by('stuid')
    elif alterstuid:
        gradelist = Grade.objects.filter(stuid=alterstuid).delete()
    else:
        gradelist = Grade.objects.all().order_by('stuid')

    return render_to_response("editgrade.html", context_instance=RequestContext(req, {"gradelist": gradelist,"username":username,"usertype":usertype}))


def altergrade(req):
     if req.method == 'POST':
        acaname= req.POST.get("acaname")
        stuid=req.POST.get("stuid")
        username=req.POST.get("username")
        grade1=req.POST.get("grade1")
        grade2=req.POST.get("grade2")
        grade3=req.POST.get("grade3")

        Grade.objects.get_or_create(acaname=acaname,stuid=stuid,username=username,grade1=grade1,grade2=grade2,grade3=grade3)
        return render(req,'base.html')
     return render(req,"alterstudent.html")
def viewclass(req):
    acaname = req.GET.get("acaname")
    username = req.COOKIES.get('username', '')
    usertype = req.COOKIES.get('usertype', '')

    stulist = Student.objects.filter(acaname=acaname).values("acaname","classnum").distinct()
    return render_to_response("viewclass.html", context_instance=RequestContext(req, {"stulist": stulist,
                                                                                      'username': username,
                                                                                      'usertype': usertype}
                                                                                ))


def viewclassstu(req):
    acaname = req.GET.get("acaname")
    classnum = req.GET.get("classnum")
    username = req.COOKIES.get('username', '')
    usertype = req.COOKIES.get('usertype', '')
    stulist = Student.objects.filter(classnum=classnum, acaname=acaname)
    return render_to_response("viewclassstu.html", context_instance=RequestContext(req, {"stulist": stulist,
                                                                                         'username': username,
                                                                                         'usertype': usertype}
                                                                                   ))


def changepsw(req):
    username = req.COOKIES.get('username')
    print username
    if req.method == 'POST':
        newpwd = req.POST.get('newpwd')
        User.objects.filter(username=username).update(password=newpwd)
        return render_to_response('login.html')
    return render_to_response("changepsw.html", {'username': username})

def review(req):
    if req.method == 'POST':
        student = req.POST.get("stuid")
        index1=req.POST.get("index1")
        index2=req.POST.get("index2")
        index3=req.POST.get("index3")
        index4=req.POST.get("index4")
        Review.objects.get_or_create(student=student,index1=index1,index2=index2,index3=index3,index4=index4)
        return render(req,'base.html')
    return render(req,"review.html")



def viewreview(req):

    if req.method=='GET':
        stuid = req.GET.get("stuid")
        username = req.COOKIES.get('username', '')
        reviewlist = Review.objects.filter(student=stuid)
        return render_to_response("viewreview.html",
                              context_instance=RequestContext(req, {'reviewlist':reviewlist, 'username': username}))
