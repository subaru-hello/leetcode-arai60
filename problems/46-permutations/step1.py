class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current: List[int], remaining_nums: List[int]):
            if not remaining_nums:
                result.append(current)
                return

            for i in range(len(remaining_nums)):
                backtrack(current + [remaining_nums[i]], remaining_nums[:i] + remaining_nums[i+1:])

        backtrack([], nums)
        return result
