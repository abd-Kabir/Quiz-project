# Generated by Django 3.2.9 on 2021-11-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='language',
            field=models.CharField(choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')], max_length=10),
        ),
    ]
