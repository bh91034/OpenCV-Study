"""
Reference : https://deep-learning-study.tistory.com/99
"""
import cv2
import sys
import os

path = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 폴더를 가져온다.

# BGR 컬러 영상으로 읽기 (기본값), shape = (rows, cols, 3)
# img = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

# 그레이스스케일 영상으로 읽기, shape = (rows, cols)
img = cv2.imread(path + os.path.sep + 'cat.bmp', cv2.IMREAD_GRAYSCALE)

# 영상 파일 속성 그대로 읽기, ex) 투명한 PNG 파일 : shape = (rows, cols, 4)
# img = cv2.imread('cat.bmp', cv2.IMREAD_UNCHANGED)

if img is None:
    print('Imager load failed!') # 이미지가 없으면 출력
    sys.exit()

cv2.namedWindow('image') # OpenCV에서 지원하는 창을 생성하는 명령어
cv2.imshow('image', img) # 첫 번째는 어떤 창에 불러올 것이냐, 두 번째는 어떤 것을 불러올 것이냐

while True:
    k = cv2.waitKey(0) # 키 입력 받기

    if k == ord("s"): # 키값='s' 이면, 변환된(e.g. 그레이스스케일) 이미지를 저장
        cv2.imwrite(path + os.path.sep + "cat_gray.png", img)

    if k == ord("x") or k == ord("q"): # 키값='x' 혹은 키값='q' 이면, 창을 닫음
        cv2.destroyAllWindows() # 모든 창을 닫음
        break

    if k == ord("w"): # 키값='w' 이면, 창을 넓힘
        window_rect = cv2.getWindowImageRect('image')
        cv2.resizeWindow('image', window_rect[2]+10, window_rect[3]+10)

    if k == ord("n"): # 키값='n' 이면, 창을 줄임
        window_rect = cv2.getWindowImageRect('image')
        cv2.resizeWindow('image', window_rect[2]-10, window_rect[3]-10)

    if k == ord("l"): # 키값='l' 이면, 창을 좌로 이동
        window_rect = cv2.getWindowImageRect('image')
        x = window_rect[0] - 8 # Window frame 의 테두리 만큼을 제거해야함
        y = window_rect[1] - 31 # Window frame 의 Title 영역 만큼을 제거해야함
        cv2.moveWindow('image', x+10, y)

    if k == ord("r"): # 키값='r' 이면, 창을 좌로 이동
        window_rect = cv2.getWindowImageRect('image')
        x = window_rect[0] - 8 # Window frame 의 테두리 만큼을 제거해야함
        y = window_rect[1] - 31 # Window frame 의 Title 영역 만큼을 제거해야함
        cv2.moveWindow('image', x-10, y)

sys.exit()