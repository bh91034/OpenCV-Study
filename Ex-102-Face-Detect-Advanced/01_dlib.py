"""
Reference :
 - ChatGPT 질문에 대한 답으로 얻은 코드
   > 질문: python opencv 에서 detect image를 하는데, haarcascade_frontalface_default.xml 로는 얼굴인식 인식율이 떨어지는 것 같아요. 더 좋은 방법을 추천해주세요.

Required Module :
 - opencv-python
 - dlib

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install dlib

dlib 설치시 에러 처리
 - https://velog.io/@yimethan/Windows10%EC%97%90-CMake-dlib-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-Python-3.10
 - 필요한 프로그램
   > cmake
   > Visual Studio 2022 - 'C++를 사용한 데트크톱 개발'
 - 주의사항
   > 설치후 재부팅 필요
"""
import cv2
import dlib
import os

# Load the detector
detector = dlib.get_frontal_face_detector()

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.
images_dir = path + os.path.sep +  'images' + os.path.sep

# Load an image
image = cv2.imread(images_dir + 'image3.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = detector(gray)

# Draw rectangles around each face
for face in faces:
    x, y, w, h = (face.left(), face.top(), face.width(), face.height())
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the output
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()