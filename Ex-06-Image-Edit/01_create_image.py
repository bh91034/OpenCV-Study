"""
Reference : https://deep-learning-study.tistory.com/103

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import os
import sys
import numpy as np

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.

# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)       # grayscale image 임의의 value
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image 모든 픽셀이 0
img3 = np.ones((240, 320), dtype=np.uint8) * 128  # dark gray 모든 픽셀이 1 * 128
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow 픽셀을 지정


# 생성된 영상 출력
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()