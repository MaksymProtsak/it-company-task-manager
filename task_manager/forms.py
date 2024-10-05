from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Task, Worker


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
            )
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
