from django import forms
from account.models import User
from operations.models import Task, ToDoItem
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = '__all__'
        exclude = ['user', 'status']


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'name', 'rank')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data
