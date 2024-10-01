from django import forms

from task_manager.models import Task


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
