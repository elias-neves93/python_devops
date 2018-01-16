#!/usr/bin/python3

import sys
"""
Teste de comentario
"""
for i in range(0,10):
    print ("Numero: {}".format(i));


lista = ["Linux", "outra", "Python"];

for i,n in enumerate(lista): #A função enumerate() retorna a posição dos elementos na lista.
    print ("{} está na posição {}".format(n,i));

    if n.lower() == "linux":
        print("Achou Linux");
        continue;
    else:
        print("Ainda não achou");


usuarios = []

nome = ""

while nome != "sair":
    nome = input("Digite o Nome: ")
    if "Elias" in usuarios:
        print(usuarios.index("Elias"))
    if nome == "sair":
        print("Saindo...")
        break;
    if not nome in usuarios:
        print ("{} Entrou no chat".format(nome))
        usuarios.append(nome)
    for u in usuarios:
        print("{} está online".format(u))

carrinho = []

produto1 = {"nome": "tenis","valor": 59}
produto2 = {"nome": "calça","valor": 100}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print("Tamanha da lista {}".format(len(carrinho)))

print("Seu carrinho possui {} itens".format(len(carrinho)))
total = 0
for c in carrinho:
    total += c["valor"]
print("O valor total é: {}".format(total))
