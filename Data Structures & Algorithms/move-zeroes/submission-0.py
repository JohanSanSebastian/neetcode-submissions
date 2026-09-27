class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        for i in range(len(nums)):
            if nums[s] == 0:
                nums.append(nums.pop(s))
            else:
                s+=1

        