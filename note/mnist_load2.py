# https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as pl
import cv2

# 저장된 모델 파일 경로 설정
model_path = 'mnist.h5'  # 실제 파일 경로로 변경

# 모델 로드
model = load_model(model_path)

def preprocess_image(img_path):
    # 이미지 읽기
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 이미지 크기 조정 (MNIST 데이터셋 이미지 크기와 동일하게)
    img = cv2.resize(img, (28, 28))

    # 이미지 값 0~1 사이로 정규화
    img = img / 255.0

    # 이미지 차원 추가 (배치 차원)
    img = np.expand_dims(img, axis=0)

    return img

def predict_digit(img_path):
    # 이미지 전처리
    img = preprocess_image(img_path)

    # 모델 예측
    prediction = model.predict(img)

    # 가장 높은 확률을 가진 클래스 선택
    predicted_class = np.argmax(prediction)

    return predicted_class

# 그림 파일 경로 설정
image_path = '5-1.png'  # 실제 그림 파일 경로로 변경

# 그림 판별
predicted_digit = predict_digit(image_path)

# 결과 출력
print("Predicted digit:", predicted_digit)

# 이미지 출력

img = cv2.imread(image_path)
import matplotlib.pyplot as plt
plt.imshow(img, cmap='gray')
plt.title(f"Predicted digit: {predicted_digit}")
plt.show()