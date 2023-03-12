from django.urls import path
from  .views import success, profile_view


urlpatterns = [
    path('<str:slug>', profile_view, name='profile_view'),
    path('success', success, name='success')
    
]
