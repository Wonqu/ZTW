from django import forms
from Prosaist.models import Status_Conflict, Status


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class StatusConflictCreateForm(forms.Form):
    status1 = MyModelChoiceField(label='First status', queryset=Status.objects.all())
    status2 = MyModelChoiceField(label='Second status', queryset=Status.objects.all())
    project = forms.IntegerField(label='Project ID')

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(StatusConflictCreateForm, self).__init__(*args, **kwargs)

        if projectid:
            self.fields['status1'].queryset = Status.objects.filter(project_id=projectid)
            self.fields['status2'].queryset = Status.objects.filter(project_id=projectid)

    class Meta:
        model = Status_Conflict
        fields = ("status1", "status2", "project")


