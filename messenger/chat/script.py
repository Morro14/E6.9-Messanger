from .models import MyUser
from django.utils.text import slugify


users = MyUser.objects.all()
for user in users:
    user.slug = slugify(user.username)
    user.save()