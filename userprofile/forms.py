from django import forms
from .models import Profile, Skill, Education
from django.forms import inlineformset_factory

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'instagram', 'github', 'linkedin', 
                  'profile_picture', 'contact_email', 'contact_phone']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']  # Remove percentage field

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'year']

EducationInlineFormSet = inlineformset_factory(
    Profile,  # Ensure this is the correct model
    Education,
    form=EducationForm,
    extra=1,
    can_delete=True
)

SkillFormSet = inlineformset_factory(Profile, Skill, form=SkillForm, extra=1, can_delete=True)
