# Generated by Django 3.1.3 on 2021-01-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20210111_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rank',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
