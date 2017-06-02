from django import forms
from Prosaist.models import Project


class ProjectCreateForm(forms.Form):
    name = forms.CharField(label='Project name', max_length=255)

    class Meta:
        model = Project
        fields = ("name")
