"""
Reference : https://deep-learning-study.tistory.com/100

Required Module :
 - matplotlib

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install matplotlib
"""
import matplotlib.pyplot as plt
import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.

#컬러 영상 출력
imgBGR = cv2.imread(path + os.path.sep + 'cat.bmp')

# 그레이스케일로 영상 불러오기
imgGray = cv2.imread(path + os.path.sep + 'cat.bmp', cv2.IMREAD_GRAYSCALE)

# cv2.imread는 BGR로 불러오므로 plt를 이용하려면 RGB로 바꿔줘야 함
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()