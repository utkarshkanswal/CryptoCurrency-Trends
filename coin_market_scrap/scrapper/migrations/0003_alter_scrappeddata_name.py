# Generated by Django 5.0.4 on 2024-04-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_alter_scrappeddata_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrappeddata',
            name='Name',
            field=models.CharField(default='NONE', max_length=200),
        ),
    ]