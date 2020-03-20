#!/usr/bin/env python3
# coding:utf-8

import wave

w = wave.open("indian.wav", "rb")
h = wave.open("result.wav", "wb")

print(w.getnchannels())  # 1：单声道
print(w.getsampwidth())  # 2：采样字节长度
print(w.getframerate())  # 11025：采样频率

h.setnchannels(w.getnchannels())
h.setsampwidth(w.getsampwidth()//2)
h.setframerate(w.getframerate()*2)
frames = w.readframes(w.getnframes())  # 读取并返回以 bytes 对象表示的最多 n 帧音频；音频总帧数

wave.big_endiana = 1
h.writeframes(frames)  # 写入音频帧并确保 nframes 是正确的
w.close()
h.close()
