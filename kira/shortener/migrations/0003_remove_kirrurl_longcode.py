# Generated by Django 2.2.4 on 2019-08-07 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_kirrurl_longcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kirrurl',
            name='longcode',
        ),
    ]
