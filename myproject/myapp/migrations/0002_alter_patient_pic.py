# Generated by Django 4.0.5 on 2022-07-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pic',
            field=models.FileField(default='media/default_doc.png', upload_to='media/images'),
        ),
    ]
