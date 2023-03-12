from django.forms import ModelForm
from chat.models import MyUser


class FileUploadForm(ModelForm):
    
    class Meta:
        model = MyUser
        fields = ['profile_picture']

