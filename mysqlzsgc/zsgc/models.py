# -*- coding:utf-8 -*-
from django.db import models



class Employee(models.Model):
    name = models.CharField(max_length=20, verbose_name='员工名字')
    age = models.IntegerField(verbose_name='年龄')

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name


class Job(models.Model):
    employee = models.ForeignKey(Employee)
    emp_job = models.CharField(max_length=50, verbose_name='工作')
    emp_num = models.IntegerField(default=0, verbose_name='员工编号')

    class Meta:
        verbose_name = '工作'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.emp_job