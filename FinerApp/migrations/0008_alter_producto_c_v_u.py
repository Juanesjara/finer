# Generated by Django 4.0.6 on 2022-10-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinerApp', '0007_costos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='c_v_u',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]