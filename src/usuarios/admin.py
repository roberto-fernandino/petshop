from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from usuarios.models import Account, Atendimentos


# Register your models here.


@admin.action(description="Marcar atendimento(s) como respondido")
def set_respondidos(modeladmin, request, queryset):
    queryset.update(status="r")


class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ["nome", "assunto", "get_status_display", "data"]
    ordering = ["data"]
    actions = [set_respondidos]


# User Custom model
class UserCrerationForm(forms.ModelForm):
    """Um form para criar novos usuarios."""

    password1 = forms.CharField(label="senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="senha confirmacao", widget=forms.PasswordInput)
    data_nascimento = forms.DateField(label='Data de nascimento')
    cpf = forms.CharField(label="cpf")

    class Meta:
        model = Account
        fields = ["email", "username", "data_nascimento", "cpf",]

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

    list_display = ["email", "username", "cpf", "is_admin", "data_criacao"]
    list_filter = ["is_admin", "data_criacao", "is_staff", "is_superuser"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Informacao pessoal", {"fields": ["data_nascimento", "cpf",]}),
        ("Permissoes", {"fields": ["is_admin", "is_staff", "is_superuser"]}),
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
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(Account, UserAdmin)
admin.site.register(Atendimentos, AtendimentoAdmin)
admin.site.unregister(Group)
