"""
URL configuration for model_inherit_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from model_inherit_app import views as v
from model_app1 import views as v1
from model_app2 import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',v.home),
    # path('about/',v1.model_manager),
    path('',v2.home1,name='home1'),
    path('user/',v2.show_user_data,name='user'),
    path('page/',v2.show_page_data,name='page'),
    path('post/',v2.show_post_data,name='post'),
    path('song/',v2.Show_song_data,name='song'),
]
