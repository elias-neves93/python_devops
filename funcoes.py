#!/usr/bin/python3

# -*- coding: UTF-8 -*-

from datetime import datetime

carrinho = []

produto1 = {"nome": "tenis","valor": 59}
produto2 = {"nome": "calça","valor": 100}

produtos = []

def cadastrar_produtos(produto):
    global produtos
    produtos.append(produto)

def listar_produtos():
    global produtos
    for p in produtos:
        print (p)

produto = ""
"""
while produto != "sair":
    produto = input("Digite o produto que queira cadastrar: ")
    cadastrar_produtos(produto)
    print ("Produto cadastrado com sucesso.")
    listar_produtos()
"""

def calcular(*args):
    if len(args) == 1:
        print ("A área do quadrado é: {}".format(args[0]*args[0]))
    elif len(args) == 2:
        print ("A área do retângulo é: {}".format(args[0]*args[1]))
    elif len(args) == 3:
        print ("A área do paralelepipedo é: {}".format(args[0]*args[1]*args[2]))
    print(args)
#calcular(2)
#calcular(4,2)
#calcular(1,2,3)

def descobre_dicionario(**Kwargs):
    print(Kwargs.keys())

    for k in Kwargs.keys():
        print("Chave: {}".format(k))
        print("Tem o valor de: {}".format(Kwargs[k]))


#descobre_dicionario(nome="Elias Neves")
#descobre_dicionario(figura="Figura")

black = lambda x: x*2

print("Valor do produto: {}".format(black(produto1["valor"])))
print("Com desc de 50%: {}".format(produto1["valor"]))


try:
    with open("teste.txt", 'r') as f:
        print (f.read())
except Exception as e:
    print ("Erro {}".format(e))

acesso = datetime(2018,1,14,00,00,00)
atual = datetime(2018,1,14,00,00,00)

if (atual - acesso).total_seconds() > 3600:
    print("Token expirou")
else:
    print ("OK")
print (datetime.today())
