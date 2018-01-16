from datetime import date

def escrever_arquivo(nome, dados):
    with open("{}.txt",.format(nome)"w") as f:
        f.write(dados)

def ler_arquivo(nome):
    with open("{}.txt".format(nome),"r") as f:
        var = f.read()
        return var

def data_atual():
    return date.today()
