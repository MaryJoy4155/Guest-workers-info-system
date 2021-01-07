"""guestworker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth import views as auth_views

from guestworker import settings
from django.conf.urls.static import static

from guest.views import IndexView, RegisterView, LoginView, UserView, SignUp, Reg_contractor, Reg_sponsor, \
    RegisterView_contractor
from guest import worker_urls,admin_urls

urlpatterns = [

    path('', IndexView.as_view()),
    path('register', RegisterView.as_view(),name='register'),
    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('worker/', worker_urls.urls()),
    path('admin/', admin_urls.urls()),
    path('SignUp', SignUp.as_view()),
    path('reg_contractor', Reg_contractor.as_view()),
    path('reg_sponsor',Reg_sponsor.as_view()),
    path('RegisterView_contractor',RegisterView_contractor.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)