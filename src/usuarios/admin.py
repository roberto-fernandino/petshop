from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from usuarios.models import Account, Atendimentos, UserCart, UserCartItems
from usuarios.mail import EnviaNewsLetterFromDataBase, EnviarNewsletter

# Register your models here.

@admin.action(description="Marcar atendimento(s) como respondido")
def set_respondidos(modeladmin, request, queryset):
    queryset.update(status="r")


@admin.action(description="Envia newsletter para emails elecionados")
def envia_newsletter(modeladmin, request, queryset):
    inquery_users = []
    for obj in queryset:
        email = obj.email
        nome = obj.nome
        inquery_users.append((email, nome))
    EnviaNewsLetterFromDataBase(inquery_users)


@admin.action(description="Envia newsletter para todos emails condizentes")
def envia_newsletter_para_condizentes(modeladmin, request):
    EnviarNewsletter()


class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "email","status", "data", "is_newsletter"]
    ordering = ["data"]
    fieldsets = [
        ("Usuario", {"fields": ["email", "nome", "phone"]}),
        ("Atendimento", {"fields": ["status", "assunto", "message"]}),
        ("Email Preferences", {"fields": ['is_newsletter']}),
    ]
    actions = [set_respondidos, envia_newsletter]
    list_filter = ["is_newsletter", "data"]


class DateInput(forms.DateInput):
    input_type = "date"


# User Custom model
class UserCrerationForm(forms.ModelForm):
    """Um form para criar novos usuarios."""

    email = forms.EmailField(
        label="email", widget=forms.EmailInput(attrs={"class": "input-field"})
    )
    username = forms.CharField(
        label="username", widget=forms.TextInput(attrs={"class": "input-field"})
    )
    password1 = forms.CharField(
        label="password", widget=forms.PasswordInput(attrs={"class": "input-field"})
    )
    password2 = forms.CharField(
        label="password confirmation",
        widget=forms.PasswordInput(attrs={"class": "input-field"}),
    )
    data_nascimento = forms.DateField(
        label="data nascimento", widget=DateInput(attrs={"class": "input-field"})
    )
    cpf = forms.CharField(
        label="cpf", widget=forms.TextInput(attrs={"class": "input-field"})
    )
    is_newsletter = forms.BooleanField(label='is newsletter', required=False, initial=True, widget=forms.CheckboxInput(attrs={
        "class": 'check-box'})
    )
    
    class Meta:
        model = Account
        fields = [
            "email",
            "password1",
            "password2",
            "username",
            "data_nascimento",
            "cpf",
            "is_newsletter",
        ]

    def clean_passwords(self):
        """Checa as duas senhas"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and (password1 != password2):
            raise ValidationError("As senhas nao conferem")
        return password2

    def save(self, commit=True):
        """Salva a senha em formato hash para maior seguranca"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    """um form para modificar usuarios"""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = [
            "email",
            "username",
            "password",
            "data_nascimento",
            "cpf",
            "is_active",
            "is_admin",
        ]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCrerationForm

    list_display = [
        "email",
        "id",
        "username",
        "cpf",
        "is_admin",
        "data_criacao",
        "last_login",
    ]
    list_filter = ["is_admin", "data_criacao", "is_staff", "is_superuser"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Informacao pessoal", {"fields": ["data_nascimento", "cpf", "last_login"]}),
        ("Permissoes", {"fields": ["is_admin", "is_staff", "is_superuser"]}),
        ("Email Preferences", {"fields": ["is_newsletter"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "username",
                    "data_nascimento",
                    "cpf",
                    "password1",
                    "password2",
                ],
            },
        )
    ]
    search_fields = ["email", "username"]
    ordering = ["-last_login"]
    filter_horizontal = ["user_permissions"]




class UserCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price']
    readonly_fields = ['total_price']

    def total_price(self, obj):
        preco = obj.calculate_total_price() / 100        
        return f'R${preco}'
    total_price.short_description = 'Preco Total'

class UserCartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart','produto', 'quantidade']

admin.site.register(UserCartItems, UserCartItemsAdmin)
admin.site.register(UserCart, UserCartAdmin)
admin.site.register(Account, UserAdmin)
admin.site.register(Atendimentos, AtendimentoAdmin)
admin.site.unregister(Group)