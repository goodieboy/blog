# Generated by Django 3.1.7 on 2021-04-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20210402_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(blank=True, verbose_name='Published Date'),
        ),
    ]