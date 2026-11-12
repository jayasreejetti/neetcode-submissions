class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum=nums1+nums2
        sum.sort()
        n=len(sum)
        mid=n//2
        if n%2==1:
            return sum[mid]
        else:
            return (sum[mid-1]+sum[mid])/2