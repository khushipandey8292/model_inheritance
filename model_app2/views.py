from django.shortcuts import render
from .models import Page,Post,Song,User
# Create your views here.

def home1(request):
    return render(request,'home.html')

def show_user_data(request):
    data1=User.objects.all()
    data2=User.objects.filter(page__page_cate='Programming')
    data3=User.objects.filter(song__song_duration=5)
    return render(request,'user.html',{'data1':data1,'data2':data2,'data3':data3})

def show_page_data(request):
    data1=Page.objects.all()
    data2=Page.objects.filter(page_cate='Programming')
    return render(request,'page.html',{'data1':data1,'data2':data2})

def show_post_data(request):
    data1=Post.objects.all()
    data2=Post.objects.filter(user__username='swet')
    return render(request,'post.html',{'data1':data1,'data2':data2})

def Show_song_data(request):
    data1=Song.objects.all()