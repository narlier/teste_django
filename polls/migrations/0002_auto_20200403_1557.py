# Generated by Django 3.0.3 on 2020-04-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name='Publicado em:'),
        ),
    ]