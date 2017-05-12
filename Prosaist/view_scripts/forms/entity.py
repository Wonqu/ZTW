from django import forms
from Prosaist.models import Entity

class EntityCreateForm(forms.Form):
    name = forms.CharField(label='Entity name', max_length=255)
    project = forms.IntegerField(label='Project ID')
    class Meta:
        model = Entity
        fields = ("name", "project")