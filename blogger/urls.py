"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from users import urls
from  . import views
from django.conf.urls.static import static
from django.conf import settings
from drafts import urls
from moderator import urls
from users import urls
from writer import urls
from admins import urls
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'users/', include('users.urls')),
    path(r'', views.red),
    path(r'drafts/', include('drafts.urls')),
    path(r'moderator/', include('moderator.urls')),
    path(r'writer/', include('writer.urls')),
    path(r'admins/', include('admins.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)