#!/usr/bin/python2.7

# -*- coding: UTF-8 -*-

from paramiko.client import SSHClient
import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("172.16.65.100",username='',password='')

stdin,stdout,stderr = client.exec_command("lss -la")


if stderr.channel.recv_exit_status() != 0:
    print stderr.channel.recv_exit_status()
    print stderr.read()
else:
    print stdout.read()
