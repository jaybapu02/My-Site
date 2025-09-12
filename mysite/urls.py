"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from mysite import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("nav_bar/",views.aboutUs,name='nav_bar'),
    path("fotter/",views.aboutUs,name='fotter'),
    path("about/",views.aboutUs,name='about'),
    path("contact/", include("jay.urls")),
    path("home/",views.home,name='home'),
    path("projects/",views.projects,name='projects'),
    path("skill/",views.skills,name='skills'),
    path('', views.home,name="home"),
]
