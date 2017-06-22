from django import forms
from Prosaist.models import Entity, Period, Status, AffectedBy


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class AffectedByCreateForm(forms.Form):
    entity = MyModelChoiceField(label='Entity', queryset=Entity.objects.all())
    period = MyModelChoiceField(label='Period', queryset=Period.objects.all())
    status = MyModelChoiceField(label='Status', queryset=Status.objects.all())
    project = forms.IntegerField(label='Project ID')

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(AffectedByCreateForm, self).__init__(*args, **kwargs)

        if projectid:
            self.fields['entity'].queryset = Entity.objects.filter(project_id=projectid)
            self.fields['period'].queryset = Period.objects.filter(project_id=projectid)
            self.fields['status'].queryset = Status.objects.filter(project_id=projectid)

    class Meta:
        model = AffectedBy
        fields = ("entity", "period", "status", "project")
