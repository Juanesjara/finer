# Generated by Django 4.0.6 on 2022-10-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinerApp', '0008_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]