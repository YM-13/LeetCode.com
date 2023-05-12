"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""

class Solution:
	def isPalindrome(self, x: int) -> bool:
		l_list = []


		if x >= 0 and x // 10 >= 0:
			while x != int():
				d = x % 10
				x = x // 10
				l_list.append(d)
			r_list = reversed(l_list)

			for a, b in zip(l_list, r_list):
				if a != b:
					return False
			return True
		else:
			return False



sol = Solution()
print(sol.isPalindrome(0))