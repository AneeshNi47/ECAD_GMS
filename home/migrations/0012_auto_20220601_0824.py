# Generated by Django 3.0.5 on 2022-06-01 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220601_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='microsection',
            name='REMARKS',
            field=models.CharField(default='Enter remarks', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='microsection',
            name='Result',
            field=models.CharField(default='Enter result', max_length=122),
            preserve_default=False,
        ),
    ]
