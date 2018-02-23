import sys

try:
    from pymongo import MongoClient
except:
    sys.exit("Install libs!")

client = MongoClient('127.0.0.1')
db=client["devops"]

db.fila.remove() # Apagar os dados escritos previamente
#db.fila.insert({"_id":1,"servico":"Intranet","status":0})
#db.fila.insert({"_id":2,"servico":"WebSite","status":0})
#db.fila.insert({"_id":3,"servico":"Backup","status":0})
#db.fila.insert({"_id":4,"servidor":"127.0.0.1","nome":"Asterisk"})

#db.fila.update({"_id":1},{"$set":{"servico":"Apache"}})

servidor1 = {"endereco":"192.168.0.10","nome":"dns"}
servidor2 = {"endereco":"192.168.0.11","nome":"mysql"}

servidores=[]

servidores.append(servidor1)
servidores.append(servidor2)

db.fila.insert({"_id":5,"analista":"Elias Neves","servidores":servidores})

for i in db.fila.find():
    print ("O analista {}, tem acesso aos servidores".format(i["analista"]))
    for s in i['servidores']:
        print(s['nome'], " - ",s['endereco'])
