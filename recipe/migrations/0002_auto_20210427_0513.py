# Generated by Django 3.2 on 2021-04-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
