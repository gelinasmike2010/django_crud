# Generated by Django 2.1.3 on 2018-12-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_year',
            field=models.IntegerField(),
        ),
    ]