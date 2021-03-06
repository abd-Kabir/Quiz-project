# Generated by Django 3.2.9 on 2021-11-04 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_app', '0002_auto_20211104_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[(1, 'Math'), (2, 'English')], max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[(1, 'Hard'), (2, 'Medium'), (3, 'Easy')], max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
