# Generated by Django 4.2.5 on 2024-02-07 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicepermission',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='devicepermission',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='devicepermission',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='devicepermission',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]