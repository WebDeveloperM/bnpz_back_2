# Generated by Django 5.0.6 on 2024-08-21 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0025_statistic_alter_site_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='titleAdd',
            field=models.CharField(default=1, max_length=200, verbose_name='Hajm birligi'),
            preserve_default=False,
        ),
    ]