# nc_tutorials/urls.py

# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
# path('', views.home, name='home'),
# ]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutorials/', include('tutorials.urls')),
    path('api/tutorials/', include('tutorials.urls')),  # make sure the trailing slash is here
]