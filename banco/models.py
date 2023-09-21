from django.db import models

class Uf(models.Model):
    id_uf = models.IntegerField(primary_key=True)
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)

class Cidade(models.Model):
    id_cidade = models.IntegerField(primary_key=True)
    nome_cidade = models.CharField(max_length=50)
    id_uf = models.ForeignKey(Uf, on_delete=models.CASCADE)

class Enderecos(models.Model):
    id_endereco = models.IntegerField(primary_key=True)
    id_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    observacoes = models.TextField()


class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Conta(models.Model):
    
    class Tipos(models.TextChoices):
        POUPANCA = "Poupança"
        CORRENTE = "Corrente"

    class Bancos(models.TextChoices):
        BANCO_1 = "Banco 1"
        BANCO_2 = "Banco 2"
        BANCO_3 = "Banco 3"
        BANCO_4 = "Banco 4"

    id_conta = models.IntegerField(primary_key=True)
    tp_conta = models.CharField(max_length=30, choices=Tipos.choices)
    banco = models.CharField(max_length=30, choices=Bancos.choices)
    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()

class Pessoa(models.Model):
    
    class Vinculos(models.TextChoices):
        VINCULO_1 = "Vinculo 1"
        VINCULO_2 = "Vinculo 2"
        
    id_pessoa = models.IntegerField(primary_key=True)
    vinculo = models.CharField(max_length=20, choices=Vinculos.choices)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    email = models.EmailField()
    id_conta = models.OneToOneField(Conta, on_delete=models.CASCADE)
    id_endereco = models.OneToOneField(Enderecos, on_delete=models.CASCADE)

class Ocorrencia(models.Model):
    
    id_ocorrencia = models.IntegerField(primary_key=True)
    data = models.DateField()
    realizada = models.CharField(max_length=1)
    ocorrencia = models.TextField()
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
