import urllib.request

content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) + len(find))
dolar = content[posicao : posicao + 4]

content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find)+ len(find))
euro = content[posicao : posicao + 4]

print("Dolar: {}".format(dolar))
print("Euro: {}".format(euro))
