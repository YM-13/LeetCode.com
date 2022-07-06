from typing import List


class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:

		nums.sort()

		return nums[-k]


nums = [3,2,1,5,6,4]
k = 2

sol = Solution()
print(sol.findKthLargest(nums, k))