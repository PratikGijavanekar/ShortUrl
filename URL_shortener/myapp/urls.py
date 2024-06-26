from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore

from . import views

urlpatterns = [
   path('hello', views.hello_world),
   path('', views.home_page),
   path('all-analytics', views.all_analytics),

   path('<slug:short_url>',views.redirect_url)
]
