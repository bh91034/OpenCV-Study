"""
Reference : https://deep-learning-study.tistory.com/102

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import os
import sys

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.

# 영상 불러오기
img1 = cv2.imread(path + os.path.sep + 'cat.bmp', cv2.IMREAD_GRAYSCALE) # 그레이스케일
img2 = cv2.imread(path + os.path.sep + 'cat.bmp', cv2.IMREAD_COLOR)     # 컬러


# 불러왔는지 확인
if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()
    
    
# 영상의 속성 참조
print('type(img1):', type(img1)) # img1의 타입 확인 <class 'numpy.ndarray>
print('img1.shape:', img1.shape) # 각 차원의 크기 (480, 640) h,w 순서
print('img2.shape:', img2.shape) # 각 차원의 크기 (480, 640, 3), h,w,컬러 순서 png파일은 3 -> 4
print('img1.dtype:', img1.dtype) # 원소의 데이터 타입. 영상 데이터는 unit8


# 영상의 크기 참조
h, w = img2.shape[:2] # 슬라이싱이므로 2-1 -> 0,1   2개만 갖고 옴
print('img2 size: {} x {}'.format(w, h)) # h : 480, w : 640

# 영상 출력
cv2.imshow('img1', img1) # 윈도우창을 생성하지 않아도 자동으로 생성
cv2.imshow('img2', img2)
cv2.moveWindow('img2', 400, 200) # 'img1', 'img2'가 겹치기 때문에 이동
cv2.waitKey()

img1 = cv2.imread(path + os.path.sep + 'cat.bmp', cv2.IMREAD_GRAYSCALE) # 그레이스케일
img2 = cv2.imread(path + os.path.sep + 'cat.bmp', cv2.IMREAD_COLOR)     # 컬러


# for문을 이용한 영상의 픽셀 값 수정
# 매우 느려서 절대 이용하면 안됌, OpenCV or Numpy에서 제공하는 함수 이용하기.
for y in range(h):
    for x in range(w):
        # y, x 순서인 이유 : 영상 행렬은 높이, 길이로 저장되므로
        img1[y, x] = 255 # BGR 모두 255 => 하양색
        img2[y, x] = (0, 0, 255) # x,y 위치의 픽셀을 (0, 0, 255) 빨강색으로 만듬
        

# 슬라이싱을 이용한 영상의 픽셀 값 수정
img1[:,:] = 255         # 모든 픽셀을 흰색
img2[:,:] = (0, 0, 255) # 모든 픽샐을 빨강색


# 영상 출력
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()


# 윈도우 창 닫기
cv2.destroyAllWindows()