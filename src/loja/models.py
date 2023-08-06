from django.db import models



# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    setor = models.CharField(max_length=50)
    preco = models.FloatField()
    descricao = models.TextField(null=True, blank=False)
    imagem = models.ImageField(upload_to="products",blank=False, null=True)

    def __str__(self):
        return f" {self.nome_produto} | {self.setor} "
    



