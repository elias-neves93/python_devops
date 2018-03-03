# -*- coding: UTF-8 -*-

import requests
import json
import sys

# Definir o caminho da URL
def _url(path):
    return 'http://localhost:3000/{}'.format(path)

# Listar todos os itens no json
def get_task():
    response = requests.get('http://localhost:3000/usuarios')
    print(response.text)

# Adicionar um item no JSON
def add_task(email="",nome=""):
    return requests.post(_url('/usuarios/'),json={"email": email,"nome":nome,})

# Apagar um item no JSON
def del_task(task_id, email, nome):
    return requests.delete(_url('/usuarios/{:d}/'.format(task_id)))

# Atualizar um item no json
def update_task(task_id, emai, nome):
    url = _url("/usuarios/{:d}/".format(task_id))
    return requests.put(url, json={"email":email,"nome":nome,})

if __name__ == '__main__':
    get_task()
