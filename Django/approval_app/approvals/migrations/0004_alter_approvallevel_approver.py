# Generated by Django 5.1.3 on 2024-11-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0003_alter_approvallevel_approver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvallevel',
            name='approver',
            field=models.CharField(max_length=100),
        ),
    ]
