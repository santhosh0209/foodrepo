# Generated by Django 3.0.7 on 2020-06-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_partyhall_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='NameAndEmail',
        ),
        migrations.AddField(
            model_name='partyhall',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partyhall',
            name='mobile_no',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
