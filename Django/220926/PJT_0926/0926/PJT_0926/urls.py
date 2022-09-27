"""PJT_0926 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pjt import views

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("ping/", views.ping),
    path("pong/", views.pong),
    path("fake_search/", views.fake_search),
    path("odd_even/<int:id>/", views.odd_even),
    path("calculate/<int:id_a>/<int:id_b>", views.calculate),
    path("before", views.before),
    path("before2", views.before2),
    path("hsum", views.hsum),
    path("makehsum", views.makehsum),
]
