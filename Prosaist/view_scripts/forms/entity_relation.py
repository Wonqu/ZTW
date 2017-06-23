from django import forms
from Prosaist.models import Entity_Relation, Entity, Period


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class EntityRelationCreateForm(forms.Form):
    name = forms.CharField(label='Relation name', max_length=155)
    period = MyModelChoiceField(label='Period', queryset=Period.objects.all())
    entity1 = MyModelChoiceField(label='First entity', queryset=Entity.objects.all())
    entity2 = MyModelChoiceField(label='Second entity', queryset=Entity.objects.all())
    project = forms.IntegerField(label='Project ID', widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(EntityRelationCreateForm, self).__init__(*args, **kwargs)

        if projectid:
            self.fields['period'].queryset = Period.objects.filter(project_id=projectid)
            self.fields['entity1'].queryset = Entity.objects.filter(project_id=projectid)
            self.fields['entity2'].queryset = Entity.objects.filter(project_id=projectid)

    class Meta:
        model = Entity_Relation
        fields = ("name", "period", "entity1", "entity2", "project")


