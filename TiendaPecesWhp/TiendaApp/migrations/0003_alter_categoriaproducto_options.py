# Generated by Django 4.2 on 2023-04-26 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaApp', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaproducto',
            options={'verbose_name': 'categoriaProd', 'verbose_name_plural': 'categoriasProd'},
        ),
    ]
