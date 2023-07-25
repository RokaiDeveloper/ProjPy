# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppMaps(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_cidade = models.CharField(max_length=255)
    uf = models.CharField(db_column='UF', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_maps'


class AppUserMaps(models.Model):
    map = models.ForeignKey(AppMaps, models.DO_NOTHING, db_column='map')
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user')

    class Meta:
        managed = False
        db_table = 'app_user_maps'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
    action_flag = models.PositiveSmallIntegerField()
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


class MapTest(models.Model):
    cod_id = models.IntegerField(db_column='COD_ID', primary_key=True)  # Field name made lowercase.
    disteubuidora = models.CharField(db_column='DISTRIBUIDORA', max_length=5)  # Field name made lowercase.
    tipo_de_ponto = models.CharField(db_column='TIPO_DE_PONTO', max_length=42)  # Field name made lowercase.
    posse = models.CharField(db_column='POSSE', max_length=20)  # Field name made lowercase.
    estrutura = models.CharField(db_column='ESTRUTURA', max_length=13)  # Field name made lowercase.
    material = models.CharField(db_column='MATERIAL', max_length=30)  # Field name made lowercase.
    esforco_dan = models.IntegerField(db_column='ESFORCO_daN')  # Field name made lowercase.
    altura_m = models.DecimalField(db_column='ALTURA_m', max_digits=3, decimal_places=1)  # Field name made lowercase.
    localizacao = models.CharField(db_column='LOCALIZACAO', max_length=10)  # Field name made lowercase.
    x = models.DecimalField(max_digits=14, decimal_places=10)
    y = models.DecimalField(max_digits=14, decimal_places=10)
    municipio = models.CharField(db_column='MUNICIPIO', max_length=16)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'map_test'


class MapaOficial(models.Model):
    cod_id = models.IntegerField(db_column='COD_ID', blank=True, null=True)  # Field name made lowercase.
    distribuidora = models.CharField(db_column='DISTRIBUIDORA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tipo_de_ponto = models.CharField(db_column='TIPO_DE_PONTO', max_length=42, blank=True, null=True)  # Field name made lowercase.
    posse = models.CharField(db_column='POSSE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estrutura = models.CharField(db_column='ESTRUTURA', max_length=13, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='MATERIAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    esforco_dan = models.IntegerField(db_column='ESFORCO_DaN', blank=True, null=True)  # Field name made lowercase.
    altura_m = models.DecimalField(db_column='ALTURA_m', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    localizacao = models.CharField(db_column='LOCALIZACAO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    x = models.DecimalField(max_digits=14, decimal_places=10, blank=True, null=True)
    y = models.DecimalField(max_digits=14, decimal_places=10, blank=True, null=True)
    municipio = models.CharField(db_column='MUNICIPIO', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapa_oficial'
