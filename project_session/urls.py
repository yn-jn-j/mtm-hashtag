"""project_session URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',board.views.home, name="home"),
    path('new/',board.views.new, name="new"),
    path('detail/<int:pk>', board.views.detail, name="detail"),
    path('edit/<int:pk>', board.views.edit, name="edit"),
    path('delete/<int:pk>', board.views.delete, name="delete"),
    path('detail/<int:pk>/comment/<int:comment_pk>/delete/', board.views.delete_comment, name="delete_comment"),

    path('tagadd/<int:pk>', board.views.tag_add, name="tag_add"),
    path('tag', board.views.tag_home, name="tag_home"),
    path('tag/<int:pk>', board.views.tag_detail, name="tag_detail"),
    path('detail/<int:pk>/tag/<int:tag_pk>/delete', board.views.tag_delete, name="tag_delete"),
]
