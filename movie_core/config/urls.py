"""
URL configuration for movie_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import logging

from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def is_alive_view(request):
    html = "Alive!!"
    logger.info("Is alive reached.")
    return HttpResponse(html)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie_core.core.urls')),
    re_path(
        r"^$",
        is_alive_view,
        name="ping",
    ),
]
