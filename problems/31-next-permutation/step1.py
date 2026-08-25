class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def find_pivot() -> int:
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i+1]:
                    return i
            return -1

        def find_swap_point(pivot) -> int:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[pivot]:
                    return i
            return -1

        def reverse_in_range(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        pivot = find_pivot()
        if pivot == -1:
            nums.reverse()
            return nums

        swap_point = find_swap_point(pivot)
        nums[pivot], nums[swap_point] = nums[swap_point], nums[pivot]
        reverse_in_range(pivot + 1, len(nums) - 1)
