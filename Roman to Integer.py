class Solution:
    def romanToInt(self, s: str) -> int:
        c = 0
        k = list(s)
        roman_map = [["I", 1], ["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]
        
        for i in range(len(k)):
            for j in range(len(roman_map)):
                if k[i] == roman_map[j][0]:
                    k[i] = roman_map[j][1]
        
        for i in range(len(k)):
            if i < len(k) - 1 and k[i] < k[i + 1]: 
                c -= k[i] 
            else:
                c += k[i]
        
        return c
