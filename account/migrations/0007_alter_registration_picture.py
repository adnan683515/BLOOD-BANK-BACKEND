# Generated by Django 5.0.6 on 2025-03-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_registration_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='picture',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
