"""django_project URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from Web_1 import views
from Web_1.views import index, about, contact, form, edit_form, delete, upload_file, input_num, form_up_img, delete_img, form_up_pdf

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('my_form/', form, name='form'),
    path('my_form/edit_form/<int:id>/', edit_form, name='edit_form'),
    path('my_form/delete/<int:id>/', delete),
    path('form_up_img/', form_up_img, name='form_up_img'),
    path('form_up_img/delete_img/<int:id>/', delete_img),
    path('upload/', upload_file, name='upload_file'),
    path('input/', input_num, name='input_num'),
    path('form_up_pdf/', views.form_up_pdf, name='form_up_pdf'),
    path('form_up_pdf/delete_pdf/<int:id>/', views.delete_pdf),
    path('form_up_video/', views.form_up_video, name='form_up_video'),
    path('form_up_video/delete_video/<int:id>/', views.delete_video),
    path('form_up_audio/', views.form_up_audio, name='form_up_audio'),
    path('form_up_audio/delete_audio/<int:id>/', views.delete_audio),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
