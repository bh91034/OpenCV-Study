"""
Reference : https://deep-learning-study.tistory.com/105

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import numpy as np

# color 설정
blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)
white_color = (255, 255, 255)

# 하양색 영상 생성
# 400X400X3 행렬, 모든 픽셀을 255(하양색), 데이터 타입 : np.unit8
img = np.full((400,400,3), 255, np.uint8)

# 직선 그리기
cv2.line(img, (50, 50), (200, 50), red_color, 5) # 두께 5
cv2.line(img, (50, 60), (150, 160), green_color)

# 사각형 그리기
cv2.rectangle(img, (50, 200), (200, 300), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1) # -1은 내부 색 칠하기

# 원 그리기
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 다각형 외각 점들의 좌표를 np.array list 형태로 지정
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2) # [pts] 리스트 값으로 입력

# 우선 출력할 텍스트 문자열 지정
text = 'Hello? OpenCV ' + cv2.__version__

# 텍스트 그리기
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
            (0, 0, 255), 1, cv2.LINE_AA)

# 영상 출력
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()