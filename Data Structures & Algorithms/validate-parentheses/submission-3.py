class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ["(","{","["]:
                stk.append(c)
            else:
                if not stk:
                    return False
                if stk[-1] == "(" and c == ")":
                    stk.pop()
                elif stk[-1] == "[" and c == "]":
                    stk.pop()
                elif stk[-1] == "{" and c == "}":
                    stk.pop()
                else:
                    return False
        return True if not stk else False
                


