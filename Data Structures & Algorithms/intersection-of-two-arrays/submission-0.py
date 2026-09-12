class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = set()
        array_2 = set(nums2)
        for n in nums1:
            if n in array_2:
                array.add(n)

        return list(array)