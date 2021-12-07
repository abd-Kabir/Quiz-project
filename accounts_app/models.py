from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from files_app.models import Uploads
from language_app.models import Language
from language_app.utils import choices as lang_choices


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, null=False)
    profile_image = models.OneToOneField(Uploads, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=lang_choices())

    class Meta:
        db_table = 'auth_employee'
