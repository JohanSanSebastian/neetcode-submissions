class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        write = 1
        
        for read in range(1, len(nums)):
            # Found a new unique element
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
                
        return write