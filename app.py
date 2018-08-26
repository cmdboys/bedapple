#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import cv2
import os
import time


class Myface:
    def __init__(self):
        self.gread = 'MNHQ&OC?7>!:-;.'
        self.ascii_char = list("$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:, ")

        self.jibie = 255 / len(self.gread)

    def get_char_from_pixel(self, r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        length = len(self.ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1) / length
        return self.ascii_char[int(gray / unit)]

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def renderStr(self, imgData):
        str = ''
        image = imgData

        # for i, ivalue in enumerate(imgData):
        #     for j, jvalue in enumerate(ivalue):
        #         # 把每个像素点转换为字符串
        #         # print(jvalue)
        #         str += self.get_char_from_pixel(jvalue[0], jvalue[1], jvalue[2])
        #     str+='\n'
        # print(str)

        for letter in image:  # 第一个实例
            for garr in letter:
                r = garr[0]
                g = garr[1]
                b = garr[2]


                grr = r * 0.299 + g * 0.587 + b * 0.114
                if grr >= 150:
                    str += '.'
                else:
                    str += self.gread[min(int(round(grr / self.jibie)), len(self.gread) - 1)]
            str += '\n'
        print(str)
    def beforeRender(self):
        print("\n" * 10000)

    def showMe(self):
        cap = cv2.VideoCapture(0)
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

        self.beforeRender()
        while True:
            ret, image = cap.read()
            resize = cv2.resize(image, (int(800 / 10), int(500 / 10)), interpolation=cv2.INTER_CUBIC)

            self.renderStr(resize)
        # 释放资源
        cap.release()
        # 关闭窗口
        cv2.destroyAllWindows()

    def showVideo(self, videoSrc):
        cap = cv2.VideoCapture(videoSrc)
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
        while (cap.isOpened()):
            self.beforeRender()
            while True:
                ret, image = cap.read()
                resize = cv2.resize(image, (int(800 / 10), int(500 / 10)), interpolation=cv2.INTER_CUBIC)

                self.renderStr(resize)
        # 释放资源
        cap.release()
        # 关闭窗口
        cv2.destroyAllWindows()