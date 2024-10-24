# Generated by Django 5.1.1 on 2024-09-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('bl', '🔴 Blocker'), ('cr', '🟠 Critical'), ('mj', '🟡 Major'), ('mn', '🟢 Minor'), ('tr', '🔵 Trivial')], max_length=2),
        ),
    ]
