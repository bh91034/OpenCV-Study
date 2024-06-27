"""
Reference :
 - ChatGPT 질문에 대한 답으로 얻은 코드
   > 질문: python opencv 에서 detect image를 하는데, haarcascade_frontalface_default.xml 로는 얼굴인식 인식율이 떨어지는 것 같아요. 더 좋은 방법을 추천해주세요.

Required Module :
 - opencv-python
 - mtcnn
 - cloudpickle
 - tensorflow

Install Example from Terminal prompt :
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install opencv-python
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install mtcnn
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install cloudpickle
 - PS C:\workspace\OpenCV-Study> & C:/Users/javaes/.conda/envs/OpenCV-Demo/python.exe -m pip install tensorflow
"""
import os

from mtcnn import MTCNN
import cv2

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.
images_dir = path + os.path.sep +  'images' + os.path.sep

# Load an image
image = cv2.imread(images_dir + 'image3.jpg')

# Initialize the detector
detector = MTCNN()

# Detect faces
faces = detector.detect_faces(image)

# Draw rectangles around each face
for face in faces:
    x, y, width, height = face['box']
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

# Display the output
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()