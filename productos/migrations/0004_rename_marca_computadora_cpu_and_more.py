# Generated by Django 5.1.1 on 2024-10-25 03:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_computadora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computadora',
            old_name='marca',
            new_name='cpu',
        ),
        migrations.RenameField(
            model_name='computadora',
            old_name='modelo',
            new_name='gpu',
        ),
        migrations.RemoveField(
            model_name='computadora',
            name='fecha',
        ),
        migrations.AddField(
            model_name='computadora',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computadora',
            name='ram',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]