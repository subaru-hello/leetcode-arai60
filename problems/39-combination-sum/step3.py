class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def find_combinations(path: List[int], remaining_target: int, remaining_candidates: List[int]):
            if remaining_target < 0:
                return
            if remaining_target == 0:
                result.append(path)
                return
            for i in range(len(remaining_candidates)):
                find_combinations(path + [remaining_candidates[i]], remaining_target - remaining_candidates[i], remaining_candidates[i:])
        find_combinations([], target, candidates)
        return result
