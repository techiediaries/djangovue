from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/public/', views.public),
    url(r'^api/private/', views.private),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),    
    
]
