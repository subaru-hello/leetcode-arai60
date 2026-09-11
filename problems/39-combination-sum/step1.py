class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(path: List[int], remaining: int, candidates: List[int]):
            if remaining == 0:
                result.append(path)
                return

            if remaining < 0:
                return
            for i in range(len(candidates)):
                backtrack(path + [candidates[i]], remaining - candidates[i], candidates[i:])
        backtrack([], target, candidates)
        return result
