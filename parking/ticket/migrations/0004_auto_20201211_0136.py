# Generated by Django 3.1.4 on 2020-12-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20201209_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]