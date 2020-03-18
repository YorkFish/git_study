#!/usr/bin/env python3
# coding:utf-8

import xmlrpc.client

# 建立 XML-RPC 服务器代理
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# 列出 XML-RPC 服务器上的方法
print(conn.system.listMethods())
