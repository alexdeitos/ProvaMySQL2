from django.db import models

class Prova(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Pergunta(models.Model):
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='media/perguntas/', blank=True, null=True)

    def __str__(self):
        return self.texto

    def texto_formatado(self):
        return self.texto.replace('\n', '<br>')

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=800)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

    def texto_formatado(self):
        return self.texto.replace('\n', '<br>')
