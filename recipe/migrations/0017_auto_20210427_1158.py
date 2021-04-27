# Generated by Django 3.2 on 2021-04-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0016_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='collection',
            field=models.ManyToManyField(to='recipe.Collection'),
        ),
    ]