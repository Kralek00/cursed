from django.db import models
from django.db.models import DateField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, Group, Permission


# модель пользователя для управления ролями
class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('viewer', 'Просматривающий'),
        ('member', 'Отвечающий'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')


# для хранения информации о дне рождения в
# формате MM-DD (месяц, день)
def validate_month_day(value):
    try:
        month, day = map(int, value.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValidationError('Некорректная дата.')
    except ValueError:
        raise ValidationError('Некорректный формат даты. Используйте MM-DD.')


# модель участника сообщества(АСКа)
# важно, что участники деляется только на отвечающих и админов
# админы также могут быть отвечающими.
class Member(models.Model):
    ROLE_CHOICES_MEMBER = (
        ('adminASK', 'Администратор'),
        ('answer', 'Отвечающий'),
    )

    ID = models.AutoField(primary_key=True)
    FCS = models.CharField('Имя', max_length=100)
    Role = models.CharField('Роль', max_length=20, choices=ROLE_CHOICES_MEMBER)
    Date_of_birth = models.CharField('День рождения', max_length=5, validators=[validate_month_day], null=True,
                                     blank=True)
    Link_to_the_page = models.CharField('Ссылка на страницу', max_length=100)
    Link_to_the_group = models.CharField('Ссылка на группу', max_length=255, null=True, blank=True)
    Date_of_joing = models.DateField('Дата присоединения')

    def __str__(self):
        return self.FCS

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class Character(models.Model):
    GENDER_CHOICES_CHARACTER = (
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
    )

    ID = models.AutoField(primary_key=True)
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='characters')
    Gender = models.CharField(max_length=20, choices=GENDER_CHOICES_CHARACTER)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Name']
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Deadline(models.Model):
    ID = models.AutoField(primary_key=True)
    Character_ID = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='deadlines')
    Answers_or_debts = models.CharField(null=True, blank=True)
    Extra_time = models.DateField('Доп. время', null=True, blank=True)
    Type_of_deadlines = models.TextField('Замечание:', null=True, blank=True)

    def __str__(self):
        return str(self.Character_ID)

    class Meta:
        ordering = ['Character_ID__Name']
        verbose_name = 'Дедлайн'
        verbose_name_plural = 'Дедлайны'


class EventOrg(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField('Название ивента', max_length=100)
    Organizer_ID = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='events_organizer')
    Tags = models.TextField('Теги ивента')
    Date_of_event = DateField('Дата ивента')
    Ideas_for_event = models.TextField('Идеи ивента', null=True, blank=True)

    def clean(self):
        if self.Organizer_ID.Role != 'adminASK':
            raise ValidationError('Организатором может быть только админ.')

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Date_of_event']
        verbose_name = 'Ивент'
        verbose_name_plural = 'Ивенты'


class EventMem(models.Model):
    DEADLINE_CHOICES_MEMBER = (
        ('passed', 'Сдал'),
        ('failed', 'Не сдал'),
    )

    Event_ID = models.ForeignKey(EventOrg, on_delete=models.CASCADE, related_name='events')
    Character_ID = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='events_character')
    Passed_or_failed = models.CharField(max_length=20, choices=DEADLINE_CHOICES_MEMBER)

    def __str__(self):
        return str(self.Character_ID)

    class Meta:
        verbose_name = 'Ивент1'
        verbose_name_plural = 'Ивенты1'
