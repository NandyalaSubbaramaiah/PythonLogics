from django.contrib import admin
from django.urls import path

from geeks_site.views import hello_geecks

urlpatterns=[path('admin/',admin.site.urls), path('geek/',hello_geecks)

]