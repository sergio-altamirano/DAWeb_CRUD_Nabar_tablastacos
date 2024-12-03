# Generated by Django 5.1 on 2024-11-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
                ('cantidad', models.CharField(max_length=100)),
                ('id_ingrediente', models.CharField(max_length=6)),
                ('id_sucursal', models.CharField(max_length=6)),
                ('Id_categoria', models.CharField(max_length=6)),
            ],
        ),
    ]