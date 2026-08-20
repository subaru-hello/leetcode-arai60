class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def traverse(path: str, open_count: int, close_count: int):
            if open_count == n and close_count == n:
                result.append(path)
                return
            if open_count < n:
                traverse(path + '(', open_count + 1, close_count)
            if close_count < open_count:
                traverse(path + ')', open_count, close_count + 1)
        traverse('', 0, 0)
        return result
