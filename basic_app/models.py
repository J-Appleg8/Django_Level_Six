from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, PositiveBigIntegerField
from django.db.models.fields.related import ForeignKey


class School(models.Model):
    name = CharField(max_length=256)
    principal = CharField(max_length=256)
    location = CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = CharField(max_length=256)
    age = PositiveBigIntegerField()
    school = ForeignKey(School, related_name="students", on_delete=CASCADE)

    def __str__(self):
        return self.name
