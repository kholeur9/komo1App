# Generated by Django 3.2.13 on 2023-12-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_retraitcredit_data_mo'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalgeneral',
            name='total_accord_credit',
            field=models.IntegerField(default=0),
        ),
    ]