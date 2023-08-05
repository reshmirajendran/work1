# from django import forms
# from app1.models import CustomUser
# from django.contrib.auth.forms import UserCreationForm
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model=CustomUser
#         fields=UserCreationForm.Meta.fields+('email','phone')

# class studentForm(forms.ModelForm):
#     class Meta:
#         model=student
#         fields='__all__'

#  class studentForm2(forms.ModelForm):
#     class Meta:
#         model=courseregistration
#         fields=['phoneno']


from django import forms
from app.models import student
from app.models import courseregistration

class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

class studentForm2(forms.ModelForm):
    class Meta:
        model=courseregistration
        fields=['phoneno']