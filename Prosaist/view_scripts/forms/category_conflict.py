from django import forms
from Prosaist.models import Category_Conflict, Category


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class CategoryConflictCreateForm(forms.Form):
    category1 = MyModelChoiceField(label='First category', queryset=Category.objects.all())
    category2 = MyModelChoiceField(label='Second category', queryset=Category.objects.all())
    project = forms.IntegerField(label='Project ID', widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(CategoryConflictCreateForm, self).__init__(*args, **kwargs)

        if projectid:
            self.fields['category1'].queryset = Category.objects.filter(project_id=projectid)
            self.fields['category2'].queryset = Category.objects.filter(project_id=projectid)

    class Meta:
        model = Category_Conflict
        fields = ("category1", "category2", "project")


