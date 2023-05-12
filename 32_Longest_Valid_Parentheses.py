'''32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        my_dict = {'(': ')'}
        ss = list(s)
        list_of_sizes = []
        sum_pr = 0
        # проверка символов и пустой строки
        if not '(' in ss or not ')' in ss or ss == []:
            return sum_pr
        for it in ss: ### not right
            if it == '(' or it == ')':
                pass
            else:
                ss.remove(it)

        while ss[0] != '(':
            del ss[0]

        while ss[-1] == '(' and len(ss) > 1:  # if
            del ss[-1]

        l = 0
        r = 0
        while ss != [] and len(ss) > 1:
            while ss[0] != '(' and len(ss) > 1:
                ss.remove(ss[0])
                list_of_sizes.append(sum_pr)
                sum_pr = 0
            for it in ss:
                if it == '(':
                    l += 1
                else:
                    r += 1
                if l == r:
                    sum_pr = sum_pr + (l + r)
                    del ss[:(l + r)]
                    l = 0
                    r = 0
                    break
            if l != r and sum_pr == 0:
                del ss[0]
                l = 0
                r = 0
            elif l != r and sum_pr > 0:
                list_of_sizes.append(sum_pr)
                sum_pr = 0
                l = 0
                r = 0
                del ss[0]
            # elif ss != []:
            #     if ss[0] == ')':
            #         ss.remove(ss[0])
            #         list_of_sizes.append(sum_pr)
            #         sum_pr = 0
        list_of_sizes.append(sum_pr)
        list_of_sizes.sort()
        return list_of_sizes[-1]



s = ")("  # ()(() = 2,   )()()) = 4,   (() = 2,   ()(()) = 6,   )()()) = 4,    (()()) = 6    )()())()()( = 4    )(())))(())()) = 6
# ()((()())) ((()((()()    ))))((()((  = 2      ())))()(()))((  = 6   )(())))(())())  = 6
sol = Solution()
print(sol.longestValidParentheses(s))