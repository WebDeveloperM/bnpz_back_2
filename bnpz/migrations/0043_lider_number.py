# Generated by Django 5.0.6 on 2024-08-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0042_lider_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='lider',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Nomer'),
            preserve_default=False,
        ),
    ]