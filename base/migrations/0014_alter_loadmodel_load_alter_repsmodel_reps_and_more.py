# Generated by Django 4.2.1 on 2024-02-28 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_user_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmodel',
            name='load',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='repsmodel',
            name='reps',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='setsmodel',
            name='sets',
            field=models.IntegerField(blank=True),
        ),
    ]
