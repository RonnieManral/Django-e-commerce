# Generated by Django 3.1.7 on 2021-05-31 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_data',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]