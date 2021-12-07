from django.db import models
from django.contrib.auth.models import User


class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name="+")
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
