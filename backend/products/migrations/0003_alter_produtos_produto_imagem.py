# Generated by Django 4.2.4 on 2024-01-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_produtos_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='produto_imagem',
            field=models.ImageField(upload_to='produtos'),
        ),
    ]
