# Generated by Django 5.1.1 on 2024-10-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img_notebook')),
            ],
        ),
        migrations.DeleteModel(
            name='Paleta',
        ),
    ]