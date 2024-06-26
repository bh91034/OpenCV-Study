"""
Reference : https://deep-learning-study.tistory.com/104

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import os
import sys

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.
image_path = path + os.path.sep +  'images' + os.path.sep

src = cv2.imread(image_path + 'cat.bmp', cv2.IMREAD_COLOR)

# cv2.IMREAD_UNCHANGED로 4채널 영상을 불러올 때 이용
logo = cv2.imread(image_path + 'opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

# 불러오기 확인
if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

# mask는 알파 채널로 만든 마스크 영상
# 그레이스케일이어야 하므로 3마지막 값만 갖고 와서 1차원으로 만들어준다.
# [:, :, 3] ==> [height, width, bgra] 로부터 [height전체, width전체, a(alpha)] 만 가져옴
mask = logo[:, :, 3]

# logo는 b, g, r 3채널로 구성된 컬러, 4채널이므로 -1 까지 갖고옴
# [:, :, 3] ==> [height, width, bgra] 로부터 alpha 만 제거한 [height전체, width전체, bgr] 을 가져옴
logo = logo[:, :, :-1]

h, w = mask.shape[:2]

# src와 dst의 크기가 다르다. 따라서 마스크 연산이 안됌
# src와 동일한 크기의 영상을 추출 = crop
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출, 좌표는 임의대로

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0] # bool 인덱싱도 이용 가능

cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()
sys.exit()