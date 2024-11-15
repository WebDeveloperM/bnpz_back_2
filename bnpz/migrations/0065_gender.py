# Generated by Django 5.0.6 on 2024-11-01 05:25

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0064_remove_faq_file_remove_message_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Nomer: ')),
                ('title', models.CharField(max_length=400, verbose_name='Sarlavha')),
                ('mainImage', models.ImageField(blank=True, default='gender.jpg', null=True, upload_to='', verbose_name='Asosiy rasm. 500x500 shart')),
                ('description_1', models.TextField(blank=True, null=True, verbose_name="Ta'rif 1")),
                ('description_2', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Ta'rif 2")),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasm 1')),
                ('description_3', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Ta'rif 3")),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasm 2')),
                ('description_4', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Ta'rif 4")),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasm 3')),
                ('description_5', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Ta'rif 5")),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasm 4')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasm 5')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('view', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active:')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bnpz.language', verbose_name='Tilni tanlang')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': '9.6 Gender tenglig',
            },
        ),
    ]
