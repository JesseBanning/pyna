#!/usr/bin/env python3

## std library imports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import commands_list

def main():
  ## create session object
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

  ## create SSH connection
  sshsession.connect(hostname='10.10.2.3', username='bender', pkey=mykey)
  manycommands = []
  our_commands = [input("please list the commands that you wish to pass:")]
  while manycommands(-1) != "done"
    manycommands = manycommands.append(our_commands)
    break
  commands_list(sshsession, manycommands)


  ## end the SSH connection
  sshsession.close()

if __name__ == '__main__':
  main()
