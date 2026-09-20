  class Solution:
    def convert(self, s: str, numRows: int) -> str:
      words = [[] for i in len(numRows))] 
      row = 0
      direction = 1
      for i, char in enumerate(s):
        words[i] = char
	if row > len(numRows):
          direction = -1
        row += direction
      
