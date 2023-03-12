from django.core.management.base import BaseCommand
from chat.models import MyUser
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Populate slug field of MyUser model instances"

    def handle(self, *args, **options):
        
        users = MyUser.objects.all()
        for user in users:
            user.slug = slugify(user.username)
            user.save()
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfuly populated slug fields for {users}.')
        )