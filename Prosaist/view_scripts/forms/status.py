from django import forms
from Prosaist.models import Status


class StatusCreateForm(forms.Form):
    name = forms.CharField(label='Status name', max_length=255)
    project = forms.IntegerField(label='Project ID', widget=forms.HiddenInput())

    class Meta:
        model = Status
        fields = ("name", "project")
