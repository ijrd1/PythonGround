class Solution:
    def moveZeroes(self, nums) -> None:
        """
        void. modify in-place
        """
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            else:
                i += 1
                j += 1
