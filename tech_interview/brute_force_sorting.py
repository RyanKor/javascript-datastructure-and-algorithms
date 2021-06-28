# 방법 2 : 하드 코딩 --> 연산 속도 O(n^2) // 보통 Brute Force (완전 탐색)이라 부르는 형태
arr = [1,4,6,8,90,5,7,2,3]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)