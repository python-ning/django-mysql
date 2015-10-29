# -*- coding:utf-8 -*-
from zsgc.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from random import randint
from django.core.urlresolvers import reverse


def index(request):
    return render(request, "index.html", {"testdata": Employee.objects.all()})


# 保存数据
@csrf_exempt
def add(request):
    if request.method == "GET":
        return render(request, "add.html")
    elif request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        st = Employee()
        st.age = age
        st.name = name
        st.save()

    return redirect(reverse('index'))


def show(request):
    datas = Employee.objects.all()
    return render_to_response('data.html', locals())


@csrf_exempt
def update(request, id):
    user = Employee.objects.filter(pk=id).first()
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        user.name = name
        user.age = age
        user.save()
        return redirect('/')
    return render(request, 'update.html', {"testdata": user})


@csrf_exempt
def delete(request, id):
    obj = Employee.objects.get(id=id)
    obj.delete()
    return redirect(reverse('index'))
