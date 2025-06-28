from models import Prova
prova = Prova.objects.get(nome="SOA-C02")
print(prova.id)