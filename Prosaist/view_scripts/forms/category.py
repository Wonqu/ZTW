from django import forms
from Prosaist.models import Category


class CategoryCreateForm(forms.Form):
    name = forms.CharField(label='Category name', max_length=255)
    project = forms.IntegerField(label='Project ID', widget=forms.HiddenInput())

    class Meta:
        model = Category
        fields = ("name", "project")
