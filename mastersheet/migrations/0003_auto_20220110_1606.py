# Generated by Django 3.2.1 on 2022-01-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mastersheet', '0002_alter_round2database_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='round2database',
            name='interviewer',
            field=models.CharField(blank=True, default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='round2database',
            name='selected',
            field=models.CharField(blank=True, default=False, max_length=10),
        ),
        migrations.AddField(
            model_name='round2database',
            name='taken',
            field=models.CharField(blank=True, default=False, max_length=10),
        ),
    ]