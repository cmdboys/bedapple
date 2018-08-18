#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import cv2
import os
import time


class Myface:
    def __init__(self):
        self.gread = 'MNHQ&OC?7>!:-;.'
        self.jibie = 255 / len(self.gread)

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def renderStr(self, imgData):
        str = ''
        image = imgData

        for letter in image:  # 第一个实例
            for garr in letter:
                r = garr[0]
                g = garr[1]
                b = garr[2]
                grr = r * 0.299 + g * 0.587 + b * 0.114
                if grr >= 150:
                    str += ' '
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
            resize = cv2.resize(image, (int(1200 / 10), int(600 / 10)), interpolation=cv2.INTER_CUBIC)

            self.renderStr(resize)
        # 释放资源
        cap.release()
        # 关闭窗口
        cv2.destroyAllWindows()
