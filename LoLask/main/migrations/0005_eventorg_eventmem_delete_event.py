# Generated by Django 5.1.4 on 2024-12-17 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_deadline_answers_or_debts'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventOrg',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, verbose_name='Название ивента')),
                ('Tags', models.TextField(verbose_name='Теги ивента')),
                ('Date_of_event', models.DateField(verbose_name='Дата ивента')),
                ('Ideas_for_event', models.TextField(blank=True, null=True, verbose_name='Идеи ивента')),
                ('Organizer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_organizer', to='main.member')),
            ],
            options={
                'verbose_name': 'Ивент',
                'verbose_name_plural': 'Ивенты',
            },
        ),
        migrations.CreateModel(
            name='EventMem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Passed_or_failed', models.CharField(choices=[('passed', 'Сдал'), ('failed', 'Не сдал')], max_length=20)),
                ('Character_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_character', to='main.character')),
                ('Event_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='main.eventorg')),
            ],
            options={
                'verbose_name': 'Ивент1',
                'verbose_name_plural': 'Ивенты1',
            },
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
