# Generated by Django 3.0.7 on 2020-06-18 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20200618_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='Email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trustemail', to='food.Trust', to_field='email'),
        ),
    ]
