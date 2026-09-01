from django.db import models
from Subjects.models import Subjects

# Create your models here.
class Topics(models.Model):
    topic_id=models.CharField(primary_key=True)
    sub_id=models.ForeignKey(
        Subjects,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    topic_name=models.CharField()
    topic_nature=models.CharField()
    date_studied=models.DateField()
    difficulty=models.CharField()
    self_study=models.CharField(null=True)
    overview=models.CharField()

    def __str__(self):
        return self.topic_name
