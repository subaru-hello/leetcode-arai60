class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path: List[int], candidates: List[int]):
            result.append(path)
            for i in range(len(candidates)):
                backtrack(path + [candidates[i]], candidates[i+1:])

        backtrack([], nums)
        return result
