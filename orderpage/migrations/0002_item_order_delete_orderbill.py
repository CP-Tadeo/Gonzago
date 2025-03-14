# Generated by Django 4.2 on 2023-04-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refNumber', models.IntegerField()),
                ('items', models.ManyToManyField(to='orderpage.item')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderBill',
        ),
    ]
