# Generated by Django 5.0.6 on 2024-07-22 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_consultation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='staffs',
        ),
        migrations.AddField(
            model_name='consultation',
            name='staff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='main.staff'),
            preserve_default=False,
        ),
    ]
