from django.shortcuts import render
from .models import Page,Post,Song,User
# Create your views here.

def home1(request):
    return render(request,'hom.html')

def show_user_data(request):
    data1=User.objects.all()
    return render(request,'user.html',{'data1':data1})

def show_page_data(request):
    data1=Page.objects.all()
    data2=Page.objects.filter(page_cate='programming')
    return render(request,'page.html',{'data1':data1,'data2':data2})

def show_post_data(request):
    data1=Post.objects.all()
    data2=Post.objects.filter(post_cate='communication skills')
    return render(request,'post.html',{'data1':data1,'data2':data2})

def Show_song_data(request):
    data1=Song.objects.all()
    data2=Song.objects.filter(song_duration=4)
    data3=Song.objects.filter(user__username='swet')
    return render(request,'song.html',{'data1':data1,'data2':data2,'data3':data3})