"""Lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from lab_1.views import index as index_lab1
from lab_1.views import portofolio as portofolio
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^lab-1/', include('lab_1.urls')),
    # re_path(r'^lab-2/', include('lab_2.urls')),
    re_path(r'^$', portofolio, name='portofolio'),
    re_path(r'^portofolio.html', index_lab1, name='index'),
    re_path(r'^my_experience/', include('my_experience.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
