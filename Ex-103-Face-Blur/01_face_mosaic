"""
Reference : https://devgyuworld.tistory.com/5

GIT url : git@github.com:devGyu97/opencv-face-recognition.git

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import os

# 얼굴 인식 필터 추가
# 정면
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# 모자이크 농도 설정
ratio = 0.04

# 모자이크 해야할 사진 불러오기
path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.
images_dir = path + os.path.sep +  'images' + os.path.sep

src = cv2.imread(images_dir + 'sample1.jpg')

cv2.imshow('BEFORE', src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

print(f'Found Faces : {len(faces)}')
for x, y, w, h in faces:
    # small = cv2.resize(src[136: 242, 160: 266], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    # src[136: 242, 160: 266] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    src[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

cv2.imwrite('result/result.jpg', src)
cv2.imshow('AFTER', src)
cv2.waitKey(0)