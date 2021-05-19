# Generated by Django 3.1.7 on 2021-03-22 11:33

from django.db import migrations, models
import django.db.models.deletion
import myjob.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myjob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiter',
            name='group',
            field=models.ForeignKey(default=myjob.models.Recruiter.default_group, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]
