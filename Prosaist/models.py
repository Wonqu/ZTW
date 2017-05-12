from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProsaistUser(User):
    pass

ProsaistUser._meta.get_field('username')


class Project(models.Model):
    name = models.CharField(max_length=255)
    pr_owner = models.ForeignKey(ProsaistUser, on_delete=models.PROTECT)


class Entity(models.Model):
    name = models.CharField(max_length=255)
    en_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Entity_Relation(models.Model):
    er_entity_1 = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='er_1')
    er_entity_2 = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='er_2')
    er_period = models.ForeignKey(Entity, on_delete=models.CASCADE)
    er_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Category(models.Model):
    name = models.CharField(max_length=255)
    ct_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Category_Conflict(models.Model):
    category_1 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cc_1')
    category_2 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cc_2')
    cc_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Status(models.Model):
    name = models.CharField(max_length=255)
    st_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Status_Conflict(models.Model):
    sc_status_1 = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='sc_1')
    sc_status_2 = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='sc_2')
    sc_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Event(models.Model):
    name = models.CharField(max_length=255)
    ev_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Period(models.Model):
    pe_event_start = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='estart')
    pe_event_end = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eend')
    pe_project = models.ForeignKey(Project, on_delete=models.PROTECT)

class AffectedBy(models.Model):
    ab_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    ab_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    ab_period = models.ForeignKey(Period, on_delete=models.CASCADE)
    ab_project = models.ForeignKey(Project, on_delete=models.PROTECT)