#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django import template
def index(request):
    string=u'少时诵诗书'
    TutorialList = ["HTML1111", "CSS", "jQuery", "Python", "Django"]
    return render(request,'file1.html',{'string':string,'TutorialList':TutorialList})

def add(requset,a,b):
    c=int(a)+int(b)
    return HttpResponse(c)