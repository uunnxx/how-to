class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        count = 0
        s_len =len(s)
        for i, pr in enumerate(s):
            if pr == '(':
                print(pr)
                stack.append(pr)
                count += 1
            elif pr == ')':
                print(pr)
                try:
                    stack.pop()
                    count += 1
                except IndexError:
                    if s_len != i:
                        count = 0

        return count


m = Solution()
t = m.longestValidParentheses(')()())')

print(t)
