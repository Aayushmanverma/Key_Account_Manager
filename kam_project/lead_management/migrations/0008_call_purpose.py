# Generated by Django 4.2 on 2024-12-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead_management', '0007_remove_call_contact_person_remove_call_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
    ]
