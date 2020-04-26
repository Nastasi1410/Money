from django.conf.urls import url
from django.urls import path
from userpage import view


urlpatterns=[

     path ('',view.page_user),
      path('write/',view.write)
             ]
