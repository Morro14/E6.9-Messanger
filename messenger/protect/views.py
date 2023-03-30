from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from chat.models import MyUser
from .forms import FileUploadForm
from django.http import HttpResponseRedirect, HttpResponse


# class ProfileView(DetailView, LoginRequiredMixin):
#     template_name = 'profile.html'
#     model = MyUser
#     context_object_name = 'user'
    
    
def profile_view(request, slug):
    user_profile = MyUser.objects.get(username=slug)
    viewer = request.user
    form = None
    
    if request.method == 'POST' and viewer == user_profile:
        # if request.POST.get('value') == 'delete_profile_picture':
        #     print(request.POST.get('value'))
        
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(user_profile)
            # instance = MyUser(profile_picture = request.FILES['profile_picture'])
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



    


    
    
    
