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

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def renderStr(self, imgData):
        str = ''
        image = imgData

        for i, ivalue in enumerate(imgData):
            for j, jvalue in enumerate(ivalue):
                # 把每个像素点转换为字符串
                str += self.ascii_char[int(jvalue % len(self.ascii_char))]
            str+='\n'
        print(str)

        # for letter in image:  # 第一个实例
        #     for garr in letter:
        #         r = garr[0]
        #         g = garr[1]
        #         b = garr[2]
        #
        #
        #         grr = r * 0.299 + g * 0.587 + b * 0.114
        #         if grr >= 150:
        #             str += '.'
        #         else:
        #             str += self.gread[min(int(round(grr / self.jibie)), len(self.gread) - 1)]
        #     str += '\n'
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
            resize = cv2.resize(image, (int(1200 / 10), int(600 / 10)), interpolation=cv2.INTER_CUBIC)

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
                resize = cv2.resize(image, (int(1440 / 10), int(1080 / 10)), interpolation=cv2.INTER_CUBIC)
                gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

                self.renderStr(gray)
        # 释放资源
        cap.release()
        # 关闭窗口
        cv2.destroyAllWindows()