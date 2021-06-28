arr = [1,4,6,8,90,5,7,2,3]
# 방법 3 : Merge Sort
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0 :
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:] # 포인터처럼 사용
            else:
                result.append(right[0])
                right = right[1:] # 포인터처럼 사용
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0 :
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(lst):
    if len(lst) <=1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    leftList = merge_sort(left)
    rightList = merge_sort(right)
    return merge(leftList, rightList)

print(merge_sort(arr))