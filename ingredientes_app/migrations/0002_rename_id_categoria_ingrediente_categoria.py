# Generated by Django 5.1 on 2024-12-03 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='id_categoria',
            new_name='categoria',
        ),
    ]
