"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INF=2147483648
        MIN_INF=-2147483647
        start = abs(divisor) << 31
        cur = abs(dividend)
        res = 0
        
        for i in range(32):
            y = cur - (start >> i)
            if y >= 0:
                cur = y 
                res += (1 << (31-i))
                
                if res >= 2 << 30:
                    if (dividend > 0) != (divisor > 0):
                        return -(2 << 30)
                    else:
                        return (2 << 30) - 1

        if (dividend > 0) != (divisor > 0):
            res = -res

        return res