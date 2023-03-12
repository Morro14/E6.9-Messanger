from django.contrib import admin
from .models import *
from django.conf import settings


admin.site.register(MyUser)
admin.site.register(Chat)
admin.site.register(Message)
