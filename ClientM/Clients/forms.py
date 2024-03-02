# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Project, Client, Subscription, UserProfile, Task



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'status',  'country', 'gender', 'mobile', 'client_category', 'company_name', 'official_website', 'profile_picture']
        widgets = {'profile_picture': forms.FileInput(attrs={'accept': 'image/*'})}

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'price_range', 'details']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

from .models import SubscriptionAssignment

class SubscriptionAssignmentForm(forms.ModelForm):
    class Meta:
        model = SubscriptionAssignment
        fields = ['project_name','description', 'start_datetime', 'end_datetime', 'client', 'subscription','status']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'client', 'status', 'project_url', 'credentials','total_price']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'mobile_number', 'profile_photo', 'about_me', 'location']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','description', 'deadline_date', 'user_assignment', 'project_assignment']