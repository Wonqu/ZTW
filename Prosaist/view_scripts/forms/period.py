from django import forms
from Prosaist.models import Period, Event


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class PeriodCreateForm(forms.Form):
    event1 = forms.ModelChoiceField(label='First event', queryset=Event.objects.all())
    event2 = forms.ModelChoiceField(label='Second event', queryset=Event.objects.all())
    project = forms.IntegerField(label='Project ID')

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(PeriodCreateForm, self).__init__(*args, **kwargs)

        if projectid:
            self.fields['event1'].queryset = Event.objects.filter(project_id=projectid)
            self.fields['event2'].queryset = Event.objects.filter(project_id=projectid)

    class Meta:
        model = Period
        fields = ("event1", "event2", "project")