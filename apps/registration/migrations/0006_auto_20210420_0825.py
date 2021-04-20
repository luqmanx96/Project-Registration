# Generated by Django 2.0 on 2021-04-20 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20210419_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.City'),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.State'),
        ),
    ]