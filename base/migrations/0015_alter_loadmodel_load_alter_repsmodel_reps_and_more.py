# Generated by Django 4.2.1 on 2024-02-28 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_loadmodel_load_alter_repsmodel_reps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodel',
            name='load',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='repsmodel',
            name='reps',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='setsmodel',
            name='sets',
            field=models.IntegerField(),
        ),
    ]