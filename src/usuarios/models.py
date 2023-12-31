from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from loja.models import Produto

# Create your models here.


# Status atendimentos

STATUS_CHOISES = [
    ("p", "Pendente"),
    ("r", "Respondida"),
]


class Atendimentos(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=13, default=None, blank=False, null=True)
    assunto = models.CharField(max_length=40, blank=False, null=True)
    message = models.TextField(null=True, blank=False)
    is_newsletter = models.BooleanField(default=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOISES, default="p")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Nome: {self.nome} -- Assunto: {self.assunto}  -- Status: {self.get_status_display()}"


class EmailErrorsLog(models.Model):
    email = models.EmailField(max_length=150)
    log = models.CharField(max_length=255, blank=False, null=True, default="None")
    error_date = models.DateTimeField(auto_now_add=True)


# Overriding Default Account Manager
class AccountManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        data_nascimento,
        data_criacao,
        cpf,
        password=None,
    ):
        if not email:
            raise ValueError("Email obrigatorio")
        if not username:
            raise ValueError("Username obrigatorio")
        if not data_nascimento:
            raise ValueError("Data de nascimento obrigatoria")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            data_nascimento=data_nascimento,
            data_criacao=data_criacao,
            cpf=cpf,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, username, data_nascimento, data_criacao, cpf, password
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            data_nascimento=data_nascimento,
            data_criacao=data_criacao,
            cpf=cpf,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


#  Overriding Default Base User
class Account(AbstractBaseUser, PermissionsMixin):
    # Fields do usuario custom
    email = models.EmailField(
        verbose_name="email", max_length=150, unique=True, blank=False
    )
    username = models.CharField(max_length=30, unique=True, blank=False)
    cpf = models.CharField(max_length=14, unique=True, blank=False, null=True)
    data_nascimento = models.DateField(blank=False, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    is_newsletter = models.BooleanField(default=False, null=False, blank=False)
    # Acount Manager aqui
    objects = AccountManager()

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # variavies cosntantes do novo BaseUserManager Model onde voce declara qual sera o username-field e fields
    # obrigatorios

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "data_nascimento", "cpf"]

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def esconde_cpf(self):
        return "*" * 7 +  self.cpf[-5:-2] + '-' + self.cpf[-2] + self.cpf[-1]


class UserCart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.email}"

    class Meta:
        verbose_name_plural = "Carrinho Usuario"

    def calculate_total_price(self) -> float:
        total = 0
        for item in self.items.all():
            total += item.produto.preco * item.quantidade
        return total

    def calculate_total_price_real(self) -> float:
        total = (int(self.calculate_total_price()) / 100 )
        return total

class UserCartItems(models.Model):
    cart = models.ForeignKey(
        UserCart, 
        on_delete=models.CASCADE, 
        related_name="items")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def total_price_items(self) -> float:
        return self.produto.preco * self.quantidade / 100

    class Meta:
        verbose_name_plural = 'Items Carrinho'