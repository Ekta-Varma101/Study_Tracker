from django.db import models

# Create your models here.
class Subjects(models.Model):
    sub_id=models.CharField(primary_key=True)
    sub_code=models.CharField()
    sub_name=models.CharField()
    sub_type=models.CharField()
    sub_nature=models.CharField()
    credit=models.IntegerField()
    prog=models.IntegerField()
    desc=models.CharField()

    def __str__(self):
            return self.sub_name
    

