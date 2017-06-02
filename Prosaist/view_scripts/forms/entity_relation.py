from django import forms
from Prosaist.models import Entity_Relation, Entity


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class EntityRelationCreateForm(forms.Form):
    entity1 = MyModelChoiceField(label='First entity', queryset=Entity.objects.all())
    entity2 = MyModelChoiceField(label='Second entity', queryset=Entity.objects.all())
    project = forms.IntegerField(label='Project ID')

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(EntityRelationCreateForm, self).__init__(*args, **kwargs)

        if projectid:
            self.fields['entity1'].queryset = Entity.objects.filter(project_id=projectid)
            self.fields['entity2'].queryset = Entity.objects.filter(project_id=projectid)

    class Meta:
        model = Entity_Relation
        fields = ("entity1", "entity2", "project")


