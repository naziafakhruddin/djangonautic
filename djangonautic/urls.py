"""
Test
"""

from django.contrib import admin
from django.urls import path

from blog.views import homepage
from blog.views import about


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about),
    path("", homepage),
]
