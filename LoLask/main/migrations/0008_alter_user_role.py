# Generated by Django 5.1.4 on 2024-12-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('viewer', 'Просматривающий'), ('member', 'Отвечающий')], default='viewer', max_length=20),
        ),
    ]
