from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'

# class CreateProfileView(View):
#     def get(self, req):
#         form = ProfileForm()
#         return render(req, "profiles/create_profile.html", {
#             'form': form
#         })

#     def post(self, req):
#         submitted_form = ProfileForm(req.POST, req.FILES)

#         if submitted_form.is_valid():
#             profile = UserProfile(img=req.FILES['user_img'])
#             profile.save()
#             return HttpResponseRedirect('/profiles')
#         else:
#             return render(req, "profiles/create_profile.html", {
#                 'form': submitted_form
    # })
