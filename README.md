# Change-Rendering-Cartoon-image
Cartoon rendering of images using OpenCV and Python

Bilateral Filter와 Adaptive Thresholding 기법을 결합하여 사진의 질감을 단순화하고 외곽선을 강조함으로써 만화 같은 시각적 효과를 구현합니다

본 프로그램은 크게 세 가지 주요 단계를 거쳐 사진을 만화 스타일로 변환합니다.

색상 단순화 :

cv2.bilateralFilter를 사용합니다. 이 필터는 경계선은 보존하면서 내부의 질감만 뭉개주는 특성이 있습니다.

본 코드에서는 드라마틱한 효과를 위해 이 과정을 7번 반복 적용하여 일반적인 사진의 세밀한 질감을 제거하고 단순한 색면으로 구성되도록 했습니다.

강조된 외곽선 추출 :

먼저 이미지를 흑백으로 변환한 뒤, cv2.medianBlur를 적용해 미세한 노이즈를 제거합니다.

이후 cv2.adaptiveThreshold를 사용하여 외곽선을 추출합니다. 이때 C값을 2로 낮게 설정하여 선이 더욱 굵고 진하게 나타나도록 커스터마이징했습니다.

최종 합성 :

cv2.bitwise_and 연산을 통해 1단계의 단순화된 색상 이미지 위에 2단계에서 추출한 검은색 외곽선 마스크를 씌웁니다.

이 과정을 통해 선명한 테두리와 단순한 색감이 조화를 이루는 카툰 렌더링 결과물이 생성됩니다.

성공 사례


<img width="802" height="632" alt="image" src="https://github.com/user-attachments/assets/ab31a491-7ee7-4b1b-96fa-232fa90cd4a4" />



실패 사례

<img width="802" height="632" alt="image" src="https://github.com/user-attachments/assets/7de5ea97-0392-449f-8970-f61e218f749c" />

알고리즘의 한계점 :

복잡한 배경 노이즈가 있는경우 나뭇잎이나 바닥의 세밀한 무늬가 많은 풍경 사진은 원치 않는 잔선들이 과도하게 추출되어 만화적인 깔끔함이 떨어지는 현상이 발생합니다.
