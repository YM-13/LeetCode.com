from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i, j in enumerate(nums):
			for i2, e in enumerate(nums[i + 1:], i + 1):
				if e + j == target:
					return [i, i2]
