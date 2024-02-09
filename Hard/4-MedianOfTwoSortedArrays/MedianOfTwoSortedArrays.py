from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge the sorted arrays
        def mergeArray(a: List[int], b: List[int]) -> List[int]:
            i, j = 0, 0
            merged_array = []

            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    merged_array.append(a[i])
                    i += 1
                else:
                    merged_array.append(b[j])
                    j += 1

            while i < len(a):
                merged_array.append(a[i])
                i += 1
            
            while j < len(b):
                merged_array.append(b[j])
                j += 1

            return merged_array

        # calculate median
        merged_array = mergeArray(nums1, nums2)
        middle = len(merged_array) // 2
        if len(merged_array) % 2 == 0:
            return (merged_array[middle] + merged_array[middle - 1]) / 2
        else:
            return merged_array[middle]