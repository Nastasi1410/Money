
from django.contrib import admin
from django.urls import path
from blogeconomy import views
from django.conf.urls import url,include
urlpatterns = [
    url(r'',include('mainApp.urls')),

    path('registration/', include('blogeconomy.urls')),

       path('pageuser/', include('userpage.urls')),

    path('admin/', admin.site.urls),


]
