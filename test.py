#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import cv2

# 打开本地摄像头，括号内表示设备编号，第一个设备为0，如果电脑有两个摄像头，第二个摄像头就是1
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10)

while(True):

    # 从摄像头中读取画面，while表示循环读取画面，也就是一张一张图片形成了一个视频
    ret, image = cap.read()

    # 设置每一张图片的颜色
    img_color = cv2.cvtColor(image, 0)

    # 显示窗口
    cv2.imshow('window', img_color)

    # 如果按下键盘上的 Q 就关闭窗口
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()

# 关闭窗口
cv2.destroyAllWindows()