# Generated by Django 5.1.5 on 2025-02-05 06:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_of_departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headdepartment',
            name='status',
            field=models.CharField(choices=[('ac', 'Active'), ('in', 'Inactive'), ('pd', 'Pending')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
