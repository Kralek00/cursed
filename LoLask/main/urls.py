from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.users_login, name='Login'),
    path('logout/', views.users_logout, name='Logout'),

    path('export_deadline_to_excel', views.export_deadline_to_excel, name='export_deadline_to_excel'),
    path('export_deadline_to_docx', views.export_deadline_to_docx, name='export_deadline_to_docx'),

    # взаимодействие с участниками
    path('members_adm/add_member', views.add_member, name='add_member'),
    path('members/edit/<int:member_id>/', views.edit_member, name='edit_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),

    # взаимодействие со списком персонажей
    path('characters_adm/add_character', views.add_character, name='add_character'),
    path('characters/edit/<int:character_id>/', views.edit_character, name='edit_character'),
    path('characters/delete/<int:character_id>/', views.delete_character, name='delete_character'),

    # взаимодействие с таблицей дедлайна
    path('deadline_adm/add_deadline', views.add_deadline, name='add_deadline'),
    path('deadlines/edit/<int:deadline_id>/', views.edit_deadline, name='edit_deadline'),
    path('deadlines/delete/<int:deadline_id>/', views.delete_deadline, name='delete_deadline'),

    # взаимодействие с таблицами ивента (организация)
    path('events_adm/add_event_org', views.add_event_org, name='add_event_org'),
    path('events/edit/<int:event_id>/', views.edit_event_org, name='edit_event_org'),
    path('events/delete/<int:event_id>/', views.delete_event_org, name='delete_event_org'),

    # взаимодействие с таблицами ивента (участники)
    path('events_adm/add_event_mem', views.add_event_mem, name='add_event_mem'),
    path('events/members/edit/<int:event_id>/<int:event_mem_id>/', views.edit_event_mem, name='edit_event_mem'),
    path('events/<int:event_id>/delete/<int:event_mem_id>/', views.delete_event_mem, name='delete_event_mem'),

    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),

    # Страница участников для админа
    path('members_adm', views.members_admin, name='MembersAdmin'),

    # Страницы персонажей для админов и участников
    path('characters_adm', views.characters_admin, name='CharactersAdmin'),
    path('characters_mem', views.characters_member, name='CharactersMember'),

    # Страницы дедлайн таблиц для админа и просматривающих
    path('deadline_adm', views.deadline_admin, name='DeadlineAdmin'),
    path('deadline', views.deadline_viewer, name='Deadline'),

    # Страницы ивентов для админа и просматривающих
    path('events_adm', views.events_admin, name='EventsAdmin'),
    path('events', views.events_viewer, name='Events'),
]
