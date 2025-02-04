# Generated by Django 5.1.5 on 2025-02-04 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('credit_hours', models.PositiveIntegerField()),
                ('grade_level', models.CharField(choices=[('9', 'Grade 9'), ('10', 'Grade 10'), ('11', 'Grade 11'), ('12', 'Grade 12')], max_length=2)),
                ('prerequisites', models.CharField(blank=True, max_length=255)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='departments.department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
