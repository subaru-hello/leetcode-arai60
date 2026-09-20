class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        words_by_rows = [[] for _ in range(numRows)]
        curr_row = 0
        direction = 1

        for char in s:
            words_by_rows[curr_row].append(char)

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        result = []
        for row_chars in words_by_rows:
            result.extend(row_chars)

        return "".join(result)
