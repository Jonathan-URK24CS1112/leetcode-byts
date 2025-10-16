class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count each color
        red, white, blue = 0, 0, 0
        for i in nums:
            if i == 0:   red += 1
            elif i == 1: white += 1
            elif i == 2: blue += 1

        idx = 0
        for _ in range(red):
            nums[idx] = 0
            idx += 1

        for _ in range(white):
            nums[idx] = 1
            idx += 1

        for _ in range(blue):
            nums[idx] = 2
            idx += 1
        
