# Generated by Django 2.2.3 on 2019-11-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rationdb',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rationdb',
            name='otp',
        ),
        migrations.AddField(
            model_name='rationdb',
            name='ration_key',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
