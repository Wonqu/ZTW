from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProsaistUser(User):
    pass


ProsaistUser._meta.get_field('username')


class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(ProsaistUser, on_delete=models.PROTECT)


class Entity(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Entity_Relation(models.Model):
    entity_1 = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='er_1')
    entity_2 = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='er_2')
    period = models.ForeignKey(Entity, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Category(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Category_Conflict(models.Model):
    category_1 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cc_1')
    category_2 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cc_2')
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    class Meta:
        unique_together = ("category_1", "category_2",)



class Status(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Status_Conflict(models.Model):
    status_1 = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='sc_1')
    status_2 = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='sc_2')
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Event(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class Period(models.Model):
    name = models.CharField(max_length=255)
    event_start = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='estart')
    event_end = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eend')
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class BelongsTo(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='bel_ent')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bel_cat')
    project = models.ForeignKey(Project, on_delete=models.PROTECT)


class AffectedBy(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
