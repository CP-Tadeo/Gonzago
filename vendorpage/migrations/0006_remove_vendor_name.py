# Generated by Django 4.1.7 on 2023-03-24 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorpage', '0005_vendor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='name',
        ),
    ]
