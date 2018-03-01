from pymongo import MongoClient
from random import randint
import configparser
import os
import sys

class MongoOps:
    _db = ""

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        self._client = MongoClient(config.get("mongodb","address"))
        self._db = self._client[config.get("mongodb","base")]

    def getQueue(self):
        queue = self._db.queue.find({})
        return queue

    def getServiceToRemove(self):
        return self._db.queue.find({"status":1})

    def getServiceToInstall(self):
        return self._db.queue.find({"status":0})


if __name__ == "__main__":
    m = MongoOps()
    print (m.getQueue().count())
