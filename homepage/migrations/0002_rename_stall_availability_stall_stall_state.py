# Generated by Django 4.1.7 on 2023-04-10 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stall',
            old_name='stall_availability',
            new_name='stall_state',
        ),
    ]
