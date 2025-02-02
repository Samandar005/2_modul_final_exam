# Generated by Django 5.1.5 on 2025-02-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='prerequisites',
        ),
        migrations.AddField(
            model_name='subject',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, to='subjects.subject'),
        ),
    ]
