# Generated by Django 2.1 on 2021-04-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boneadmin', '0002_auto_20210419_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubecontent',
            name='content_description',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
