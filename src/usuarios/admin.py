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
    list_display = ["nome", "assunto", "status", "data", 'is_newsletter']
    ordering = ["data"]
    fieldsets = [
        ("Usuario", {"fields": ["email", "nome", "phone"]}),
        ("Atendimento", {"fields": ["status", "assunto", "message"]}),
    ]
    actions = [set_respondidos]
    list_filter = ['is_newsletter', "data"]



class DateInput(forms.DateInput):
    input_type = 'date'

# User Custom model
class UserCrerationForm(forms.ModelForm):
    """Um form para criar novos usuarios."""
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={
        "class": "input-field"
    })) 
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        "class": "input-field"
    })) 
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={
        "class": "input-field"
    }))
    password2 = forms.CharField(label="password confirmation", widget=forms.PasswordInput(attrs={
        "class": "input-field"
    }))
    data_nascimento = forms.DateField(label='data nascimento', widget=DateInput(attrs={
        "class": "input-field"
    }))
    cpf = forms.CharField(label="cpf", widget=forms.TextInput(attrs={
        "class": "input-field"
    }))

    class Meta:
        model = Account
        fields = ["email","password1", "password2","username", "data_nascimento", "cpf",]

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

    list_display = ["email", "id", "username", "cpf", "is_admin", "data_criacao", "last_login"]
    list_filter = ["is_admin", "data_criacao", "is_staff", "is_superuser"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Informacao pessoal", {"fields": ["data_nascimento", "cpf", "last_login"]}),
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
    search_fields = ["email", "username"]
    ordering = ["-last_login"]
    filter_horizontal = ["user_permissions"]



admin.site.register(Account, UserAdmin)
admin.site.register(Atendimentos, AtendimentoAdmin)
admin.site.unregister(Group)
