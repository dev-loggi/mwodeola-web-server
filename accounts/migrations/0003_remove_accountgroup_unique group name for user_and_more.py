# Generated by Django 4.0.1 on 2022-02-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accountdetail_user_id'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='accountgroup',
            name='Unique group name for user',
        ),
        migrations.RemoveConstraint(
            model_name='accountgroup',
            name='Unique sns_group name for user',
        ),
        migrations.AddConstraint(
            model_name='accountgroup',
            constraint=models.UniqueConstraint(fields=('mwodeola_user', 'app_package_name'), name='Unique app package name to user'),
        ),
        migrations.AddConstraint(
            model_name='accountgroup',
            constraint=models.UniqueConstraint(fields=('mwodeola_user', 'group_name'), name='Unique group name to user'),
        ),
        migrations.AddConstraint(
            model_name='accountgroup',
            constraint=models.UniqueConstraint(fields=('mwodeola_user', 'sns'), name='Unique sns_group name to user'),
        ),
    ]