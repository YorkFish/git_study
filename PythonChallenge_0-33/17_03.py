#!/usr/bin/env python3
# coding:utf-8

from xmlrpc.client import ServerProxy

contact = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(contact.phone("Leopold"))
