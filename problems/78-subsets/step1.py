class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path: List[int], remainings: List[int]):
            result.append(path)
            for i in range(len(remainings)):
                backtrack(path + [remainings[i]], remainings[i+1:])
        backtrack([], nums)
        return result
