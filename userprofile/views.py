from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Skill
from .forms import ProfileForm, SkillFormSet, EducationInlineFormSet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Profile, Education, Skill

@login_required
def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    skills = Skill.objects.filter(profile=profile)
    educations = Education.objects.filter(profile=profile)
    context = {
        'profile': profile,
        'skills': skills,
        'educations': educations,
    }
    return render(request, 'userprofile/profile.html', context)

@login_required
def edit_profile(request, username):
    user = request.user

    # Ensure user_profile exists
    user_profile, created = Profile.objects.get_or_create(user=user)
    
    # Add checks to see if user_profile is None
   
    
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        education_formset = EducationInlineFormSet(request.POST, instance=user_profile)
        skill_formset = SkillFormSet(request.POST, instance=user_profile)

        if profile_form.is_valid() and education_formset.is_valid() and skill_formset.is_valid():
            profile_form.save()
            education_formset.save()
            skill_formset.save()
            return redirect('profile_view', username=user.username)
    else:
        profile_form = ProfileForm(instance=user_profile)
        education_formset = EducationInlineFormSet(instance=user_profile)
        skill_formset = SkillFormSet(instance=user_profile)

    return render(request, 'userprofile/edit_profile.html', {
        'profile_form': profile_form,
        'education_formset': education_formset,
        'skill_formset': skill_formset,
    })



def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            Profile.objects.get_or_create(user=user)  # Create profile after user registration
            login(request, user)  # Log in the user after registration
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        user_form = UserCreationForm()

    context = {'user_form': user_form}
    return render(request, 'userprofile/register.html', context)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def custom_logout(request):
    logout(request)
    return redirect('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('profile_view', kwargs={'username': self.request.user.username})
