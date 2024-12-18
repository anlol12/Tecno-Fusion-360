# Generated by Django 5.1.2 on 2024-11-11 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_remove_producto_estado_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('nuevo', 'Nuevo'), ('usado', 'Usado')], default='nuevo', max_length=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='Tienda.categoria'),
        ),
    ]
