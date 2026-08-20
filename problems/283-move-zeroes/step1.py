class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = [num for num in nums if num != 0]
        zero_count = len(nums) - len(non_zero)
        for _ in range(zero_count):
            non_zero.append(0)
        nums[:] = non_zero
        return nums
