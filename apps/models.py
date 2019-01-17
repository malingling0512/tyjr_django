# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Userinfo(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=22)
    email=models.EmailField()
    class Meta:
        db_table='userinfo'

class Banner(models.Model):
    #1、滚动条
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=225, help_text="滚动叫标题")
    image = models.CharField(max_length=225, help_text="滚动条图片存储地址")
    class Meta:
        db_table='banner'

class Business(models.Model):
    #2、产品业务
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=225, help_text="首页产品业务标题")
    img = models.CharField(max_length=225, help_text="图标")
    content = models.CharField(max_length=225, help_text="内容")
    class Meta:
        db_table='business'

class Jobs(models.Model):
    #3、招聘
    id=models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=225, help_text="职位名称")
    number = models.CharField(max_length=225, help_text="招聘人数")
    time = models.DateTimeField(max_length=225, help_text="创建时间")
    views = models.CharField(max_length=225, help_text="浏览量")
    content = models.CharField(max_length=225, help_text="内容")
    job_status = models.CharField(max_length=225,help_text="招聘状态")
    class Meta:
        db_table='jobs'

class JobsStatus(models.Model):
    #4、职位状态
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=225, help_text="状态")
    class Meta:
        db_table='jobs_status'

class News_class(models.Model):
    #5、新闻类别
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=225, help_text="新闻类别")
    class Meta:
        db_table='news_class'

class News(models.Model):
    #6、新闻
    id=models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120, help_text="新闻标题")
    author=models.CharField(max_length=100, help_text="作者")
    time=models.CharField(max_length=225, help_text="创建时间")
    views=models.CharField(max_length=12, help_text="浏览量")
    content=models.CharField(max_length=225, help_text="内容")
    type = models.CharField(max_length=20, help_text="所属类别")
    image=models.CharField(max_length=225,help_text="配图")
    class Meta:
        db_table='news'

class Product(models.Model):
    #7、产品
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=225, help_text="产品名称")
    img = models.CharField(max_length=225, help_text="图标")
    advantage = models.CharField(max_length=225, help_text="优势")
    goods = models.CharField(max_length=225, help_text="抵押物")
    money = models.CharField(max_length=225, help_text="最高可贷")
    class Meta:
        db_table='product'

class Video(models.Model):
    #8、视频
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=225, help_text="视频标题")
    video = models.CharField(max_length=225, help_text="视频地址")
    class Meta:
        db_table='video'

class Message(models.Model):
    #9、留言
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, help_text="姓名")
    phone = models.CharField(max_length=225, help_text="电话")
    email = models.EmailField(help_text="邮箱")
    content = models.CharField(max_length=225, help_text="留言")
    class Meta:
        db_table='message'
