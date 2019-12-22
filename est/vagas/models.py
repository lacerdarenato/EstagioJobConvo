from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings

# Create your models here.

SALARIO_OPCOES = (
    ('1', 'ATÉ 1000,00'),
    ('2', 'DE 1000,01 ATÉ 2000,00'),
    ('3', 'DE 3000,01 ATÉ 3000,00'),
    ('4', 'ACIMA DE 3000,01')
)
ESCOLARIDADE_OPCOES = (
    ('1', 'Ensino Fundamental'),
    ('2', 'Ensino Medio'),
    ('3', 'Tecnólogo'),
    ('4', 'Ensino Superior'), 
    ('5', 'Pós / MBA / Mestrado'),
    ('6', 'Doutorado'), 
)

class vagas(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('atalho')
    faixaSalarial = models.CharField(max_length=1, choices=SALARIO_OPCOES)
    escolaridadeMinima = models.CharField(max_length=1, choices=ESCOLARIDADE_OPCOES)
    requisitos = models.TextField('requisitos')

    def __str__(self):
        return self.name

class candidato(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    pretencaoSalarial = models.IntegerField('Pretencao salarial')
    experiencia = models.CharField('experiencia', max_length=100)
    escolaridade = models.CharField('Ultima escolaridade', max_length=100)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Nome de Usuário', max_length=20, unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('email', blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username
    
    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

class Meta:
    verbose_name = 'Usuário'
    Verbose_name_plural = 'Usuários'

class Enrollment(models.Model):

        STATUS_CHOICES = (
            (0, 'pendente'),
            (1, 'inscrito'),
            (2, 'aprovado'),
            (3, 'reprovado'),
        )


        user = models.ForeignKey(
            settings.AUTH_USER_MODEL, verbose_name='Usuário',
            related_name='enrollments'
        )
        vagas = models.ForeignKey(
            vagas, verbose_name='vaga', related_name='enrollmens'
        )
        status = models.IntegerField(
            'Situação', choices=STATUS_CHOICES, default=0, blank=True)

        created_at = models.DateTimeField('Criado em', auto_now_add=True)
        updated_at = models.DateTimeField('Atualizado', auto_now= True)

        class Meta:
            verbose_name = 'Inscrição'
            verbose_name_plural = 'Inscrições'
            unique_together = (('user', 'vagas'), )


'''class candidatar(models.Model):

    STATUS_CHOICES = (
        (0, 'pendente'),
        (1, 'inscrito'),
        (2, 'aprovado'),
        (3, 'reprovado'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Usuário',related_name='candidatar')
    vagas = models.ForeignKey(vagas, verbose_name='Vaga', related_name='candidatar')
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado', auto_now= True)

    def activate(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'vagas'), )'''


 
    