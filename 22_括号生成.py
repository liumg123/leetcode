"""
括号生成：
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def parenthesis(self,sub_ans,leftNum,rightNum,ans):
        if leftNum==0 and rightNum==0:
            return ans.append(sub_ans)
        if rightNum>leftNum:
            self.parenthesis(sub_ans+')',leftNum,rightNum-1,ans)
        if leftNum>0:
            self.parenthesis(sub_ans+'(',leftNum-1,rightNum,ans)
        print('sub_ans',sub_ans)
        return ans
    def generateParenthesis(self, n: int) -> List[str]:
        leftNum=n
        rightNum=n
        return self.parenthesis('',leftNum,rightNum,[])
        