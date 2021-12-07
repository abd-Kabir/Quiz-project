from django.db import models

# Create your models here.
from quiz_4.models import Auditable


class Uploads(models.Model):
    original_name = models.CharField(max_length=300)
    content_type = models.CharField(max_length=100)
    new_name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    code = models.CharField(max_length=70, unique=True)
    size = models.IntegerField()

    class Meta:
        db_table = 'uploads'
