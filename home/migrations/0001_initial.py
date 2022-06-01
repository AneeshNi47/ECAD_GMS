# Generated by Django 3.0.5 on 2022-05-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CAD_NO', models.CharField(max_length=122)),
                ('PANEL_NO', models.CharField(max_length=12)),
                ('DATE_CODE', models.CharField(max_length=12)),
                ('PCB_SI_NOS', models.CharField(max_length=122)),
                ('PCB_THICKNESS', models.CharField(max_length=122)),
                ('LAYER_COUNT', models.CharField(max_length=12)),
                ('PROJECT', models.CharField(max_length=12)),
                ('APPLIED_SERIAL_NOS', models.CharField(max_length=12)),
                ('Result_day', models.DateField()),
                ('MANUFACTURER_NAME', models.CharField(max_length=12)),
            ],
        ),
    ]
