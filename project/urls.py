from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,index  , name='index'),
    path('contact/' ,contact  , name='contact'),
     path('donate/' ,support_developer  , name='support_developer'),
]
