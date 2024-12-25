from django import forms
from django_select2.forms import Select2Widget
from django.forms import ModelForm, TextInput, DateInput, Textarea, Select, PasswordInput, NumberInput, HiddenInput
from .models import Member, Character, Deadline, EventOrg, EventMem


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя'
        })
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        })
    )


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['FCS',
                  'Role',
                  'Date_of_birth',
                  'Link_to_the_page',
                  'Link_to_the_group',
                  'Date_of_joing']

        widgets = {
            "FCS": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя участника',
            }),
            "Role": Select(attrs={
                'class': 'form-control',
            }),
            "Date_of_birth": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'День рождения',
            }),
            "Link_to_the_page": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на страницу',
            }),
            "Link_to_the_group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на группу',
            }),
            "Date_of_joing": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата присоединения',
            }),
        }


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['Member_ID',
                  'Gender',
                  'Name']

        widgets = {
            "Member_ID": Select2Widget(attrs={
                'class': 'form-control',
            }),
            "Gender": forms.Select(attrs={
                'class': 'form-control',
            }),
            "Name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
        }


class DeadlineForm(forms.ModelForm):
    class Meta:
        model = Deadline
        fields = ['Character_ID',
                  'Sub_answer',
                  'Miss_answer',
                  'Type_of_deadlines',
                  'Extra_time']

        widgets = {
            "Character_ID": Select2Widget(attrs={
                'class': 'form-control',
            }),
            "Sub_answer": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ответы',
            }),
            "Miss_answer": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Долги',
            }),
            "Type_of_deadlines": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Тип дедлайна',
            }),
            "Extra_time": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Доп. время',
            }),
        }


class EventOrgForm(forms.ModelForm):
    class Meta:
        model = EventOrg
        fields = ['Name',
                  'Organizer_ID',
                  'Tags',
                  'Date_of_event',
                  'Ideas_for_event']

        widgets = {
            "Name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название ивента',
            }),
            "Organizer_ID": Select2Widget(attrs={
                'class': 'form-control',
            }),
            "Tags": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Теги ивента',
            }),
            "Date_of_event": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата ивента',
            }),
            "Ideas_for_event": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание ивента',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(EventOrgForm, self).__init__(*args, **kwargs)
        # Фильтруем организаторов, чтобы показывать только админов
        self.fields['Organizer_ID'].queryset = Member.objects.filter(Role='adminASK')


class EventMemForm(forms.ModelForm):
    class Meta:
        model = EventMem
        fields = ['Event_ID',
                  'Character_ID',
                  'Passed_or_failed', ]

        widgets = {
            "Event_ID": Select2Widget(attrs={
                'class': 'form-control',
            }),
            "Character_ID": Select2Widget(attrs={
                'class': 'form-control',
            }),
            "Passed_or_failed": forms.Select(attrs={
                'class': 'form-control',
            }),
        }
