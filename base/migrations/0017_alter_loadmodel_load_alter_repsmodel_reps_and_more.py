# Generated by Django 4.2.1 on 2024-03-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_loadmodel_load_alter_repsmodel_reps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodel',
            name='load',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='repsmodel',
            name='reps',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='setsmodel',
            name='sets',
            field=models.IntegerField(null=True),
        ),
    ]