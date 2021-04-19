# Generated by Django 2.0 on 2021-04-19 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20210419_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='State',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ic',
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(default='Please Select', on_delete=django.db.models.deletion.CASCADE, to='registration.State'),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.ForeignKey(default='Please Select', null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.City'),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.ForeignKey(default='Please Select', null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.State'),
        ),
    ]
