#!/usr/bin/env python3
# coding:utf-8

from xmlrpc import client

# 建立 XML-RPC 服务器代理
conn = client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

# 1. 获取 XML-RPC 服务器上的方法帮助
# print(conn.system.methodHelp("phone"))

# 2. 获取可能的签名数组
# print(conn.system.methodSignature("phone"))

# 3. 上一题说 Bert is evil
print(conn.phone("Bert"))
