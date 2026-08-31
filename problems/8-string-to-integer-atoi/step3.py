class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 -1
        MIN_INT = -2 ** 31

        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        if index == len(s):
            return 0
        
        sign = 1
        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == "+":
            index += 1
        
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1
        
        num *= sign
        if num > MAX_INT:
            return MAX_INT
        if num < MIN_INT:
            return MIN_INT
        
        return num
        