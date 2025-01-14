#1
import numpy as np

arr1 = np.arange(1,16).reshape(5,3) #1부터 15까지 5x3 배열
arr2 = np.arange(17,23).reshape(3,2) #17부터 22까지 3x2 배열

dot = arr1.dot(arr2)  #dot 함수를 사용해 행열곱 연산 진행

print(dot, dot.shape) # arr1과 arr2의 행열곱 연산 결과 및 결과값의 shape 반환