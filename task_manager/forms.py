from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Task, Worker, Position


class PositionSearchForm(forms.Form):
    position = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search position"}
        )
    )


class TaskTypeSearchForm(forms.Form):
    task_type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search task type"}
        )
    )


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Write a task name"
                }
            ),
            "task_type": forms.Select(
                attrs={"class": "form-control border p-3 pt-2 pb-2 w-100"}
            ),
            "priority": forms.Select(
                attrs={"class": "form-control border p-3 pt-2 pb-2 w-100"}
            ),
        }


class TaskSearchForm(forms.Form):
    task = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search a task by name"}
        )
    )


class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
        )


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["username", "first_name", "last_name", "email", "position",]
        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Write a task name"
                }
            )
        }


class WorkerSearchForm(forms.Form):
    worker = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search worker"}
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        empty_label="Select Position"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Worker
        fields = ('username', 'email', 'position', 'password1', 'password2')