"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

class Solution:


	def twoSum(self, nums, target):  # (self, nums: List[int], target: int) -> List[int]:


		my_list = []
		for k, v in enumerate(nums):
			my_list.append(k)

		for i in my_list:
			for ii in my_list[(i +1):]:
				if nums[i] + nums[ii] == target:
					return [i, ii]




c_s = Solution()

print(c_s.twoSum([3, 3], 6))
