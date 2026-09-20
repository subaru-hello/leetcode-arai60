class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        words_in_rows = [[] for _ in range(numRows)]
        curr_row = 0
        direction = 1

        for char in s:
            words_in_rows[curr_row].append(char)

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        result = []
        for chars_in_row in words_in_rows:
            result.extend(chars_in_row)

        return "".join(result)
