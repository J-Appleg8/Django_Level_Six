from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, PositiveBigIntegerField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse


class School(models.Model):
    name = CharField(max_length=256)
    principal = CharField(max_length=256)
    location = CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})


class Student(models.Model):
    name = CharField(max_length=256)
    age = PositiveBigIntegerField()
    school = ForeignKey(School, related_name="students", on_delete=CASCADE)

    def __str__(self):
        return self.name
