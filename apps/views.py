# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import News,News_class, Jobs, Message, Business, Banner, Video, Product
from django.conf import settings

# Create your views here.


# 首页
def indexview(request):
    b_list=Banner.objects.all().values('image')
    new_video=Video.objects.filter(id=1)
    return render(request,"index.html",locals())

# #关于我们(静)
# def aboutview(request):
#     return render(request,"about.html")

#业务范畴(产品类型)
def productview(request):
    p_1=Product.objects.filter(id__lt=4)
    p_2 = Product.objects.filter(id__in=(4,5,6))
    p_3 = Product.objects.filter(id__in=(7,8,9))
    return render(request,'business-scope.html', locals())

#新闻中心（新闻）
def newsview(request):
    new_list=News.objects.filter()
    return render(request,"news.html",locals())

def new_detail_view(request, id):
    new_list=News.objects.filter(id=id)
    return render(request,"news-end.html",locals())

# 招聘信息（职位）
def jobview(request):
    job_list=Jobs.objects.filter()
    return render(request,"recruit.html",locals())

# 联系我们(留言板块)
import pymysql
def contactview(request):
    return render(request,"contact.html",locals())



