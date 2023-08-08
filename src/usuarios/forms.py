from django import forms
from usuarios.models import Atendimentos


class AtendimentoForm(forms.ModelForm):
    nome = forms.CharField(max_length=30,
                            min_length=3,
                            widget=forms.TextInput(attrs={
                                "class": "input-field",
                                "name": "nome",
                                "required": True,
                                "maxlength": "30",
                                "minlength": '3'
                              }))

    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={
        "class": "input-field",
        "required": True,
    })) 

    phone = forms.CharField(max_length=13,
                            min_length=11,
                            widget=forms.TextInput(attrs={
                                "class": "input-field",
                                "name": "phone",
                                "required": True,
                                "maxlength": 13,
                                "minlength": 11
                              }))
    
    assunto = forms.CharField(max_length=50,
                            min_length=5,
                            widget=forms.TextInput(attrs={
                                "class": "input-field",
                                "name": "assunto",
                                "required": True,
                                "maxlength": 50,
                                "minlength": 5,
                              }))
    message = forms.CharField(widget=forms.Textarea(attrs={
                            "name": "mensagem",
                            "rows": 6,
                            "class": "input-field",
    }))
    is_newsletter = forms.BooleanField(
                            required=False,
                            widget=forms.CheckboxInput(attrs={
                                "class": "check-box"
                            }),
                            initial=True,
                            )
    class Meta:
        model = Atendimentos
        fields = ['nome', 'email', 'phone', 'assunto', 'message', 'is_newsletter']
