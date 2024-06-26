"""
Reference : https://deep-learning-study.tistory.com/103

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.

# 영상 복사
img1 = cv2.imread(path + os.path.sep + 'images' + os.path.sep + 'HappyFish.jpg')

# img1[40:120, 30:150] 의 의미는 img1 의 image data 에서 특정 범위의 영역만 지정하는 의미이다
#  - 40 : 시작 y 좌표
#  - 120 : 끝 y 좌표
#  - 30 : 시작 x 좌표
#  - 150 : 끝 x 좌표
img2 = img1[40:220, 30:350]  # numpy.ndarray의 슬라이싱
img3 = img1[40:220, 30:350].copy()

img2.fill(0) # img1에서 img2 범위만큼 0으로 채워줌, img1에도 영향을 준다

# cv2.circle 원을 그려주는 함수, 50,50 좌표, 반지름 20, BGR값, 두깨는 2
cv2.circle(img2, (50, 50), 20, (0, 0, 255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()