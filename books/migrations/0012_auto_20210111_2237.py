# Generated by Django 3.1.4 on 2021-01-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20210111_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rank',
            field=models.IntegerField(default=0, null=True),
        ),
    ]