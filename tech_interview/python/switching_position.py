arr = [1,4,2,3,5,6,0]

# 방법 1 : 단순 하드 코딩 --> while 반복문을 사용해서 배열을 뒤집는다.

i, j = 0, len(arr)-1
while i<j:
    print("변경 전 : ", arr[i],arr[j])
    arr[i],arr[j] = arr[j],arr[i]
    print("변경 후 : ",arr[i],arr[j])
    print("배열 변경 진행 상황", arr)
    i +=1
    j -=1
print(arr)

# 방법 2 : arr[::-1]을 적용해서 뒤집는다.
# arr[::-1]

