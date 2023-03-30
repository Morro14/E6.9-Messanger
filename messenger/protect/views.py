from django.shortcuts import render, redirect
from chat.models import MyUser
from .forms import FileUploadForm

    
def profile_view(request, slug):
    user_profile = MyUser.objects.get(username=slug)
    viewer = request.user
    form = None
    
    if request.method == 'POST' and viewer == user_profile:

        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(user_profile)
            user_profile.profile_picture = request.FILES['profile_picture']
            user_profile.save()
            return redirect(f'/profile/{slug}')
    elif viewer == user_profile:
        form = FileUploadForm()
    
        
    context = {"user": user_profile, "form": form}
    return render(request, context=context, template_name='profile.html')


def profile_picture_delete(request, username):
    user = MyUser.objects.get(username=username)
    user.profile_picture = 'no_profile_picture.png'
    user.save()
    return redirect(f'/profile/{username}')



    


    
    
    
