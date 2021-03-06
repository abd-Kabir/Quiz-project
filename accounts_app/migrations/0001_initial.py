# Generated by Django 3.2.9 on 2021-11-02 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language_app', '0001_initial'),
        ('files_app', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('phone', models.CharField(max_length=15)),
                ('language', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='language_app.language')),
                ('profile_image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='files_app.uploads')),
            ],
            options={
                'db_table': 'auth_employee',
            },
        ),
    ]
