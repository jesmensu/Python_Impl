from typing import List


# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     if(m==0):
#         return nums2
#     if(n == 0):
#         return nums1
#     if(nums1[m-1]<= nums2[0]):
#         nums1[m:] = nums2[:]
#         return nums1
#     if(nums1[0]>= nums2[n-1]):
#         nums1[:] = nums2[:] + nums1[:m]
#         return nums1
#     lenNums1 = m
#     p = 0
#     i = 0
#     while(i< m+n):
#         for j in range(p, n):
#             valueIndex = nums2[j]
#             if(i == lenNums1):
#                 nums1.insert(i+1,valueIndex)
#                 i += 1
#                 t = nums1.pop(-1)
#                 lenNums1 +=1
#             elif(valueIndex <= nums1[i]):
#                 nums1.insert(i,valueIndex)
#                 i += 1
#                 t = nums1.pop(-1)
#             else:
#                 p = j 
                
#                 break
#         i += 1
#     return nums1

# print(merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))

# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     if(m==0):
#         return nums2
#     if(n == 0):
#         return nums1
#     p=0
#     lastNums1 = nums1[m-1]
#     for j in range(n):
#         for i in range(p, m+n):
#             if(nums1[p]>= nums2[j]):
#                 nums1.insert(p,nums2[j])
#                 t = nums1.pop(-1)
#                 p += 1
#                 break
#             elif(lastNums1==nums1[p]):
#                 nums1[p+1:] = nums2[j-1:]
#                 break
#             p += 1
#     print(nums1)
#     return nums1

# print(merge([1,2,3, 0,0,0], 3, [4,5,6], 3))


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    while n > 0:
          if nums1[m-1] >= nums2[n-1] and m>0:
              nums1[m+n-1] = nums1[m-1]
              m -= 1
          else:
              nums1[m+n-1] = nums2[n-1]
              n -= 1

    return nums1

print(merge([1,2,3, 0,0,0], 3, [4,5,6], 3))
