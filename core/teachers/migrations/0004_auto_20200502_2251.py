# Generated by Django 2.2.10 on 2020-05-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20200502_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='code',
            field=models.CharField(blank=True, default='T962094', max_length=7, verbose_name='Teacher code'),
        ),
    ]
