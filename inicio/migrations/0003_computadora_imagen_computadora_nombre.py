# Generated by Django 5.1.1 on 2024-10-25 02:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_computadora_delete_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='computadora',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img_computadora'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
