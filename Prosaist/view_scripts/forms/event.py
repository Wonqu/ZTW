from django import forms
from Prosaist.models import Event


class EventCreateForm(forms.Form):
    name = forms.CharField(label='Event name', max_length=255)
    project = forms.IntegerField(label='Project ID', widget=forms.HiddenInput())

    class Meta:
        model = Event
        fields = ("name", "project")
