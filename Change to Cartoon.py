import cv2
import numpy as np

def Change_cartoon(img):
    # 1. 색상 단순화 
    color = img
    for _ in range(7): # 7번 반복 적용 (더 뭉개고 싶으면 숫자를 키우세요)
        color = cv2.bilateralFilter(color, d=9, sigmaColor=150, sigmaSpace=150)

    # 2. 선명한 외곽선 추출
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7) # 선을 굵게 만들기 위해 블러 강화
    
    # 두께와 진하기 조절 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 2)

    # 3. 색상과 선 합성
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

# 이미지 불러오기 (파일 이름 확인!)
img_path = 'test.jpg'  
img = cv2.imread(img_path)

if img is None:
    print("사진을 찾을 수 없습니다.")
else:
    # 사진이 너무 크면 처리가 느릴 수 있어 크기 조절 
    img = cv2.resize(img, (800, 600)) 
    
    result = Change_cartoon(img)

    cv2.imshow("Change Cartoon", result)
    cv2.imwrite("Change_result.jpg", result) # 결과 저장
    cv2.waitKey(0)
    cv2.destroyAllWindows()