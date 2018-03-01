# -*- coding: UTF-8 -*-

from service import Service as ServiceClass
from serviceDao import ServiceDao
from dockerOps import DockerOps

class provisionOps:

    _id = ""

    def __init__(self, id):
        self._id = id

    def InstallService(self):
        service = ServiceClass()
        service._id = self._id

        sd = ServiceDao(service)
        service = sd.get()

        print ("Sera instalado o Produto ({}) para o Client ({})".format(service._product._name,service._client._name))
        docker = dockerOps()
        res = docker.createContainer(service._id,service._product._image)

    def RemoveService():
        pass
