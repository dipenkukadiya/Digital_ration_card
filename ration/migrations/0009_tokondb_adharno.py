# Generated by Django 3.0.5 on 2020-04-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0008_tokondb_tokon_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokondb',
            name='adharno',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
