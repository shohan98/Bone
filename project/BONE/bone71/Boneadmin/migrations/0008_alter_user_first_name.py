# Generated by Django 3.2 on 2021-04-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boneadmin', '0007_auto_20210412_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
