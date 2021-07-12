class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        elif x < 0:
            str_reverse_x = str((-1) * x)[::-1]
            ret = (-1) * int(str_reverse_x)
            return ret if abs(ret) <= 2**31 else 0
        else:
            ret = int(str(x)[::-1])
            return ret if abs(ret) <= 2**31 else 0
