# Generated by Django 4.2.4 on 2024-01-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_pedidos_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]
