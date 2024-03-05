# Generated by Django 4.2.5 on 2024-02-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_created_at_alter_newuser_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]