# Generated by Django 3.2.5 on 2021-07-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.CharField(default='Jul 10, 2021, 04:24 PM', editable=False, max_length=32),
        ),
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.CharField(default='Jul 10, 2021, 04:24 PM', editable=False, max_length=32),
        ),
    ]
