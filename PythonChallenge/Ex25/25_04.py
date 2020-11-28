#!/usr/bin/env python3
# coding:utf-8

from PIL import Image


def wav2img(filename):
    with open(filename, "rb") as f:
        img = Image.new("RGB", (60, 60))
        img.frombytes(f.read()[44:])
        return img


def jigsaw_puzzle():
    jigsaw = Image.new("RGB", (300, 300))
    for i in range(25):
        row, col = divmod(i, 5)  # div + mod
        piece = wav2img(f"lake{i+1}.wav")
        jigsaw.paste(piece, (col*60, row*60))
    # jigsaw.show()
    jigsaw.save("25_result.jpg")


if __name__ == "__main__":
    jigsaw_puzzle()
