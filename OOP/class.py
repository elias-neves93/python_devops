# --*-- coding: UTF-8 -*-

class Servidor:
    memoria = None
    disco = None
    cpu = None

    def contratar_memoria(self,memoria):
        self.memoria += memoria

    def contratar_disco(self,disco):
        self.disco += disco

    def contratar_cpu(self,cpu):
        self.cpu += cpu

class Cloud(Servidor):
    def __init__(self):
        self.memoria = 512
        self.cpu = 1
        self.disco = 50

class Fisico(Servidor):
    def __init__(self):
        self.memoria = 4096

dns = Servidor()
dns1 = Cloud()
dns2 = Fisico()

dns.memoria = 2048
dns.disco = 50
dns.cpu = 2

dns.contratar_memoria(2)

dns2.contratar_memoria(4)

print (dns.memoria)
print (dns1.memoria)
print (dns2.memoria)
