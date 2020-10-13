# Generated by Django 3.0.3 on 2020-09-08 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('asso', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Entree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entree', models.DateTimeField()),
                ('sortie', models.DateTimeField()),
                ('Personne', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pointage.Personne', verbose_name='passage')),
            ],
        ),
    ]