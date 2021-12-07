from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'languages'
