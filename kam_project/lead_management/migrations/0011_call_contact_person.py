# Generated by Django 4.2 on 2024-12-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead_management', '0010_call_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='contact_person',
            field=models.CharField(default='xyz', max_length=100),
        ),
    ]
