from django.contrib import admin
from django.urls import path , include
from app.views import *
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,index  , name='index'),
    path('contact/' ,contact  , name='contact'),
    path('financial-support/' ,support_developer  , name='support_developer'),
    path('captcha/', include('captcha.urls')),
    path('blog/' ,BlogPosts , name='blog'),
    path('post/<int:post_id>/', blog_detail, name='blog_detail'),
    path('services/' ,services_page , name='services_page'),
] 

urlpatterns +=  static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
