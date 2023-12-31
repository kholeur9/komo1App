# Generated by Django 4.2.8 on 2024-01-02 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=9, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TotalGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_general', models.IntegerField(default=0)),
                ('total_accord_credit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TotalCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_credit', models.IntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
            options={
                'ordering': ['client'],
            },
        ),
        migrations.CreateModel(
            name='RetraitCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(choices=[(50, '50 crédits'), (75, '75 crédits'), (100, '100 crédits'), (125, '125 crédits'), (150, '150 crédits'), (175, '175 crédits'), (200, '200 crédits')], default=50)),
                ('data_forfait', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, choices=[('En attente', 'En attente'), ('Approuvé', 'Approuvé'), ('Rejeté', 'Rejeté')], default='En attente', max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_credit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.totalcredit')),
            ],
        ),
        migrations.CreateModel(
            name='Forfait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forfait', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('forfait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.forfait')),
            ],
        ),
    ]
