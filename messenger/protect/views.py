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
    if request.method == 'POST' and viewer == user_profile:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(user_profile)
            # instance = MyUser(profile_picture = request.FILES['profile_picture'])
            user_profile.profile_picture = request.FILES['profile_picture']
            user_profile.save()
            return redirect(f'/profile/{slug}')
    else:
        form = FileUploadForm()
    context = {"user": user_profile, "form": form}
    return render(request, context=context, template_name='profile.html')


def success(request):
    return HttpResponse('Successfully uploaded')



    


    
    
    
