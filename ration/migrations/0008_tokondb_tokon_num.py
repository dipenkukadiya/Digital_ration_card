# Generated by Django 3.0.5 on 2020-04-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0007_auto_20200425_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokondb',
            name='tokon_num',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
