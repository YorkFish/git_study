#!/usr/bin/env python3
# coding:utf-8

import email

message = open("email.txt", "rb").read().decode()  # 将本题注释的所有内容保存为 email.txt
mail = email.message_from_string(message)
audio = mail.get_payload(0).get_payload(decode=True)

f = open("indian.wav", "wb")  # 音频内容：sorry
f.write(audio)
f.close()
