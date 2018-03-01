from mongoOps import MongoOps
from provisionOps import provisionOps

def Start():
    mongo = MongoOps()
    queue = mongo.getQueue()

    print ("Existem {} serviços na fila".format(queue.count()))

    for service in mongo.getServiceToInstall():
        print ("Instalando serviço {}".format(service["_id"]))
        prov = provisionOps(service["_id"])
        res = prov.InstallService()

if __name__ == "__main__":
    Start()
