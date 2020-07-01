from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(
        required=True,
         help_text="Requerido, 254 caracteres como máximo y debe ser valido."
        )
    
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("El email ya esta regsitrado.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(
                attrs={
                    'class':'form-control-file mt-3'
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3,
                    'placeholder':'Biografia'
                }
            ),
            'link': forms.URLInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enlace'
                }
            )
        }
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].required = False

class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
         help_text="Requerido, 254 caracteres como máximo y debe ser valido."
    )

    class Meta:
        model = User
        fields = {'email'}
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError("El email ya esta regsitrado.")
            
        return email