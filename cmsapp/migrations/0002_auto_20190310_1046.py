# Generated by Django 2.1.5 on 2019-03-10 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-id']},
        ),
    ]
