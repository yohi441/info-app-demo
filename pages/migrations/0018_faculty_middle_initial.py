# Generated by Django 2.2.4 on 2019-09-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20190902_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='middle_initial',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]