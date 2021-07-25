"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""


# passed!
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arr2_in = []
        arr2_not_in = []

        for i in arr2:
            if i in arr1:
                temp = arr1.count(i)
                while temp != 0:
                    arr2_in.append(i)
                    temp -= 1
        for i in arr1:
            if i not in arr2:
                arr2_not_in.append(i)
        arr2_not_in.sort()
        return arr2_in + arr2_not_in