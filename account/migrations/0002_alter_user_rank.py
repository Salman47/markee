# Generated by Django 5.0.3 on 2024-03-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]