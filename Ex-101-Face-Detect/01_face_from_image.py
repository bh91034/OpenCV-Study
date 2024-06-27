"""
Reference : https://gr-st-dev.tistory.com/915

Required Module :
 - opencv-python

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
"""
import cv2
import os

def detect_faces(image_path):
    # 이미지 파일을 로드합니다.
    image = cv2.imread(image_path)

    # 이미지를 회색으로 변환합니다. (얼굴 인식은 흑백 이미지에서 수행되므로)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 인식을 위해 얼굴 검출기를 로드합니다.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 이미지에서 얼굴을 검출합니다.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 검출된 얼굴 주위에 사각형을 그립니다.
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 결과 이미지를 화면에 출력합니다.
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.
images_dir = path + os.path.sep +  'images' + os.path.sep

# 얼굴을 인식할 이미지를 지정합니다.
image_path = images_dir + 'image1.jpg'

# 얼굴 인식 함수를 호출합니다.
detect_faces(image_path)