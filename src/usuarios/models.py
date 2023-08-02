from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


# Overriding Default Account Manager


class AccountManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        data_nascimento,
        cpf,
        password=None,
    ):
        if not email:
            raise ValueError("Email obrigatorio")
        if not username:
            raise ValueError("Username obrigatorio")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            data_nascimento=data_nascimento,
            cpf=cpf,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, data_nascimento, cpf, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            data_nascimento=data_nascimento,
            cpf=cpf,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Status atendimentos

STATUS_CHOISES = [
    ("p", "pendente"),
    ("r", "respondida"),
]


class Atendimentos(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    assunto = models.CharField(max_length=40, blank=False, null=True)
    message = models.TextField(null=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOISES, default="p")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Nome: {self.nome} -- Assunto: {self.assunto}  -- Status: {self.get_status_display()}"


#  Overriding Default Base User
class Account(AbstractBaseUser):
    # Fields do usuario custom
    email = models.EmailField(
        verbose_name="email", max_length=150, unique=True, blank=False
    )
    username = models.CharField(max_length=30, unique=True, blank=False)
    cpf = models.CharField(max_length=13, unique=True, blank=False, null=True)
    data_nascimento = models.DateField(blank=False, null=True)

    # Acount Manager aqui
    objects = AccountManager()

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # aqui declaramos as constantes do novo BaseUserManager Model

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "data_nascimento", "cpf"]

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
