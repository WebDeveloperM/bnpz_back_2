# Generated by Django 5.0.6 on 2024-09-01 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0046_alter_certificate_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Nomer'),
            preserve_default=False,
        ),
    ]