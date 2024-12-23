from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainCharacter(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    member_id = models.ForeignKey('MainMember', models.DO_NOTHING, db_column='Member_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_character'


class MainDeadline(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    deadlines = models.DateField(db_column='Deadlines')  # Field name made lowercase.
    type_of_deadlines = models.TextField(db_column='Type_of_deadlines')  # Field name made lowercase.
    character_id = models.ForeignKey(MainCharacter, models.DO_NOTHING, db_column='Character_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_deadline'


class MainDebts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    amount_of_debts = models.IntegerField(db_column='Amount_of_debts', blank=True, null=True)  # Field name made lowercase.
    extra_time = models.DateField(db_column='Extra_time', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    deadline_id = models.ForeignKey(MainDeadline, models.DO_NOTHING, db_column='Deadline_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_debts'


class MainEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    tags = models.TextField(db_column='Tags')  # Field name made lowercase.
    date_of_event = models.DateField(db_column='Date_of_event')  # Field name made lowercase.
    ideas_for_event = models.TextField(db_column='Ideas_for_event', blank=True, null=True)  # Field name made lowercase.
    character_id = models.ForeignKey(MainCharacter, models.DO_NOTHING, db_column='Character_ID_id')  # Field name made lowercase.
    member_id = models.ForeignKey('MainMember', models.DO_NOTHING, db_column='Member_ID_id')  # Field name made lowercase.
    organizer_id = models.ForeignKey('MainMember', models.DO_NOTHING, db_column='Organizer_ID_id', related_name='mainevent_organizer_id_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_event'


class MainMember(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fcs = models.CharField(db_column='FCS', max_length=100)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=20)  # Field name made lowercase.
    date_of_birth = models.CharField(db_column='Date_of_birth', max_length=5, blank=True, null=True)  # Field name made lowercase.
    link_to_the_page = models.CharField(db_column='Link_to_the_page', max_length=100)  # Field name made lowercase.
    link_to_the_group = models.CharField(db_column='Link_to_the_group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_joing = models.DateField(db_column='Date_of_joing')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_member'


class MainUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    role = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'main_user'


class MainUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(MainUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_user_groups'
        unique_together = (('user', 'group'),)


class MainUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(MainUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_user_user_permissions'
        unique_together = (('user', 'permission'),)
