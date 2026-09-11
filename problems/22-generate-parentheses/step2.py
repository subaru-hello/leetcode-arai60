class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        def traverse(open_count: int, close_count: int):
            if open_count == n and close_count == n:
                result.append(''.join(path))
            if open_count < n:
                path.append('(')
                traverse(open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(')')
                traverse(open_count, close_count + 1)
                path.pop()
        traverse(0, 0)
        return result
