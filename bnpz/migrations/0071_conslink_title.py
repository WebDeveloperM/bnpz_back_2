# Generated by Django 4.2 on 2024-12-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0070_conslink_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='conslink',
            name='title',
            field=models.CharField(default=1, max_length=200, verbose_name='Website nomi'),
            preserve_default=False,
        ),
    ]