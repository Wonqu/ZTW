from django import forms
from Prosaist.models import Entity, Category, BelongsTo


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class BelongsToCreateForm(forms.Form):
    entity = MyModelChoiceField(label='Entity', queryset=Entity.objects.all())
    category = MyModelChoiceField(label='Category', queryset=Category.objects.all())
    project = forms.IntegerField(label='Project ID', widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(BelongsToCreateForm, self).__init__(*args, **kwargs)

        if projectid:
            self.fields['entity'].queryset = Entity.objects.filter(project_id=projectid)
            self.fields['category'].queryset = Category.objects.filter(project_id=projectid)

    class Meta:
        model = BelongsTo
        fields = ("entity", "category", "project")
