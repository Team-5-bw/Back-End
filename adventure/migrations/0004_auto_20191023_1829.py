# Generated by Django 2.2.5 on 2019-10-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_auto_20191023_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
