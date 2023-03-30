from django.urls import path
from  .views import profile_view, profile_picture_delete


urlpatterns = [
    path('<str:slug>', profile_view, name='profile_view'),
    path('profile_picture_delete/<str:username>', profile_picture_delete, name="profile_picture_delete")
    
]
