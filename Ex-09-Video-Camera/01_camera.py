"""
Reference : https://deep-learning-study.tistory.com/107

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import numpy as np
import sys

# 카메라 열기
# 0은 기본 카메라(장치관리자에 저장되어있는 순서대로), 카메라가 두 대면 1~2
cap = cv2.VideoCapture(0) # 클래스 생성
# cap.open(0) # 0번 카메라 열기, videoCapture(0)을 하면 안해도 됌

 # 카메라가 열렸는지 확인
if not cap.isOpened():
    print("Camera open failed!") # 열리지 않았으면 문자열 출력
    sys.exit()

# 비디오 매 프레임 처리
while True: # 무한 루프
    ret, frame = cap.read() # 두 개의 값을 반환하므로 두 변수 지정

    if not ret: # 새로운 프레임을 못받아 왔을 때 braek
        break
        
    # 정지화면에서 윤곽선을 추출
    edge = cv2.Canny(frame, 50, 150)
    
    inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)

    # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
    if cv2.waitKey(10) == 27:
        break

cap.release() # 사용한 자원 해제
cv2.destroyAllWindows()