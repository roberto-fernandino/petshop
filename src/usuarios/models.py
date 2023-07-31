from django.db import models

# Create your models here.


# Status atendimentos

STATUS_CHOISES = [
    ('p', 'pendente'),
    ('r', 'respondida'),
]

class Atendimentos(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    assunto = models.CharField(max_length=40, blank=False, null=True) 
    message = models.TextField(null=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOISES, default='p')
    data = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f'{self.nome} -> {self.assunto} {self.status}'
    
