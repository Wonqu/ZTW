from django import forms
from Prosaist.models import Period


class PeriodCreateForm(forms.Form):
    category1 = forms.ModelChoiceField(label='First category', queryset=Period.objects.all())
    category2 = forms.ModelChoiceField(label='Second category', queryset=Period.objects.all())
    project = forms.IntegerField(label='Project ID')

    class Meta:
        model = Period
        fields = ("event1", "event2", "project")
