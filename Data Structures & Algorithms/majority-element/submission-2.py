class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total = {}
        for num in nums:
            total[num] = 1 + total.get(num, 0)
            print(total)
        return max(total, key=total.get)
        