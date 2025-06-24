from django.db import models

class Atas(models.Model):
    numero = models.CharField(max_length=80)
    titulo = models.CharField(max_length=300)
    texto = models.CharField(max_length=10000)
    data_emissao = models.DateField()
    presentes = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'atas'


class Cadastro(models.Model):
    matricula = models.CharField(max_length=10)
    nome = models.CharField(max_length=80)
    nascimento = models.DateField()
    sexo = models.CharField(max_length=15)
    pai = models.CharField(max_length=80)
    mae = models.CharField(max_length=80)
    identidade = models.CharField(max_length=20)
    cpf = models.CharField(max_length=15)
    endereco = models.CharField(max_length=120)
    funcao = models.CharField(max_length=20)
    ingresso = models.DateField()
    unidade = models.CharField(max_length=80)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    foto = models.CharField(max_length=8)
    ativo = models.CharField(max_length=1)
    observacoes = models.TextField()
    pwd = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cadastro'


class CertEmitidos(models.Model):
    dataentrada = models.DateField()
    nascimento = models.DateField()
    nome = models.CharField(max_length=120)
    mae = models.CharField(max_length=120)
    pai = models.CharField(max_length=120)
    registro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cert_emitidos'


class Certbat(models.Model):
    dataentrada = models.DateField()
    nome = models.CharField(max_length=120)
    local = models.CharField(max_length=120)
    oficiante = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'certbat'


class Congregados(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=80)
    observacao = models.CharField(max_length=8000)

    class Meta:
        managed = False
        db_table = 'congregados'


class Entradas(models.Model):
    data = models.DateField()
    observacoes = models.CharField(max_length=120)
    vidas = models.IntegerField()
    dirigente = models.CharField(max_length=80)
    valor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'entradas'


class Logs(models.Model):
    hora = models.CharField(max_length=120)
    indice = models.CharField(max_length=80)
    texto = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'logs'


class Saidas(models.Model):
    data = models.DateField()
    observacao = models.CharField(max_length=180)
    valor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'saidas'


class Tarefas(models.Model):
    data = models.DateField()
    local = models.CharField(max_length=80)
    operador = models.CharField(max_length=100)
    observacao = models.IntegerField()
    finalizada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarefas'


class Unidades(models.Model):
    nome = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'unidades'


class Usuarios(models.Model):
    registro = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=6)
    nome = models.CharField(max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=12, blank=True, null=True)
    cadastrador = models.CharField(max_length=8)
    nivel = models.IntegerField()
    local = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
