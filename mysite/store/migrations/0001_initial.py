# Generated by Django 4.1.13 on 2024-05-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('brand', models.CharField(blank=True, max_length=30)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=600)),
                ('note', models.TextField(blank=True, max_length=600)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('provider', models.CharField(choices=[('TH', 'th-tool.by'), ('TT', 'www.store.by'), ('AR', 'etp.armtek.by'), ('HR', 'gammatest.by'), ('FR', 'Force-Yato'), ('ST', 'kubala.by')], max_length=2)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
