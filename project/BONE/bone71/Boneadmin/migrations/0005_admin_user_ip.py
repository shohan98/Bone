# Generated by Django 2.1 on 2021-04-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boneadmin', '0004_auto_20210412_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='user_ip',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]