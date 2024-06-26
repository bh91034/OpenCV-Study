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

img2 = img1        # img1의 주소를 참조하므로 img1을 수정하면 img2도 변경
img3 = img1.copy() # 값을 복사해서 새로운 주소에 복사하므로 img1을 수정해도 안변함

img1.fill(255) # 모든 픽셀을 255로

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()