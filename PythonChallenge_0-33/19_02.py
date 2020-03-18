#!/usr/bin/env python3
# coding:utf-8

import wave

indian = wave.open("indian.wav", 'r')
new = wave.open("new_indian.wav", 'w')

new.setparams(indian.getparams())
new.writeframes(indian.readframes(indian.getnframes())[::-1])

indian.close()
new.close()
