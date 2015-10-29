# -*- coding:utf-8 -*-
from zsgc.models import Employee, Job
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from random import randint


def index(request):
    return render(request, "index.html", {"testdata": Employee.objects.all()})


# 保存数据
@csrf_exempt
def add(request):
    name = request.POST['name']
    age = request.POST['age']
    new_obj = Employee.objects.create(name=name, age=age)
    return HttpResponseRedirect("/")


def control(request):
    id = request.POST.get("id")
    if id == "":
        return add(request)
    else:
        return edit(request)


def edit(request):
    obj_info = Employee.objects.get(pk=request.POST.get("id"))
    obj_info.name = request.POST.get("name")
    obj_info.age = request.POST.get("age")
    obj_info.save()
    return HttpResponseRedirect("/")


def delete(request):
    targetid = request.GET['id']
    try:
        Employee.objects.filter(id=targetid).delete()
    except:
        return HttpResponse("False")
    return HttpResponseRedirect("/")
