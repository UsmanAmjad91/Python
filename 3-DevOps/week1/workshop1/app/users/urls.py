from django.urls import path
from django.http import JsonResponse
def index(request): return JsonResponse({'ok': True, 'app':'users'})
urlpatterns = [ path('api/users/health', index) ]
