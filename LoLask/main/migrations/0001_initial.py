import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Gender', models.CharField(choices=[('Male', 'Мужской'), ('Female', 'Женский')], max_length=20)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('FCS', models.CharField(max_length=100, verbose_name='Имя')),
                ('Role', models.CharField(choices=[('adminASK', 'Администратор'), ('answer', 'Отвечающий')], max_length=20, verbose_name='Роль')),
                ('Date_of_birth', models.CharField(blank=True, max_length=5, null=True, validators=[main.models.validate_month_day], verbose_name='День рождения')),
                ('Link_to_the_page', models.CharField(max_length=100, verbose_name='Ссылка на страницу')),
                ('Link_to_the_group', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на группу')),
                ('Date_of_joing', models.DateField(verbose_name='Дата присоединения')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Deadlines', models.DateField(verbose_name='Срок сдачи')),
                ('Type_of_deadlines', models.TextField(verbose_name='Тип дедлайна')),
                ('Character_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deadlines', to='main.character')),
            ],
            options={
                'verbose_name': 'Дедлайн',
                'verbose_name_plural': 'Дедлайны',
            },
        ),
        migrations.CreateModel(
            name='Debts',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount_of_debts', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество долгов')),
                ('Extra_time', models.DateField(blank=True, null=True, verbose_name='Доп. время')),
                ('Notes', models.TextField(blank=True, null=True, verbose_name='Буквы')),
                ('Deadline_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debts', to='main.deadline')),
            ],
            options={
                'verbose_name': 'Долг',
                'verbose_name_plural': 'Долги',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, verbose_name='Название ивента')),
                ('Tags', models.TextField(verbose_name='Теги ивента')),
                ('Date_of_event', models.DateField(verbose_name='Дата ивента')),
                ('Ideas_for_event', models.TextField(blank=True, null=True, verbose_name='Идеи ивента')),
                ('Character_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_character', to='main.character')),
                ('Member_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_member', to='main.member')),
                ('Organizer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_organizer', to='main.member')),
            ],
            options={
                'verbose_name': 'Ивент',
                'verbose_name_plural': 'Ивенты',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='Member_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='main.member'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('viewer', 'Просматривающий')], default='viewer', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
