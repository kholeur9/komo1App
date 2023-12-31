# Generated by Django 3.2.13 on 2023-12-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_totalgeneral_total_accord_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='retraitcredit',
            name='status',
            field=models.CharField(blank=True, choices=[('En attente', 'En attente'), ('Approuvé', 'Approuvé'), ('Rejeté', 'Rejeté')], default='En attente', max_length=20, null=True),
        ),
    ]