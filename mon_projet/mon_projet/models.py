from django.db import models

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    school_level = models.CharField(max_length=100)
    health_issue = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        app_label = 'mon_projet'