# Generated by Django 4.2 on 2024-12-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead_management', '0011_call_contact_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='res_name',
            field=models.CharField(default='xyz', max_length=100),
        ),
    ]
