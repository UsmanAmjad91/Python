from django.urls import path, include  # add include here
from . import views
# urlpatterns = [
#     path('tutorials/', include('tutorials.urls')),
#     path('users/', include('users.urls')),
#     path('api/tutorials/', views.tutorials_list, name='tutorials-list'),
#     path('api/tutorials/<int:pk>', views.tutorials_detail, name='tutorials-detail'),
#     path('api/tutorials/published', views.tutorials_published, name='tutorials-published'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorial_list, name='tutorial_list'),        # GET & POST
    path('published/', views.tutorials_published, name='tutorials_published'),
    # path('<int:pk>/', views.tutorial_detail, name='tutorial_detail'),  # optional
]

