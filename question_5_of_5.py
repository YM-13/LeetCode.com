class MovingTotal:

	def __init__(self):
		self.list_of_num_sum = []
		self.list_numbers = []


	def append(self, numbers):
		self.numbers = numbers
		self.list_numbers.extend(self.numbers)
		if self.list_of_num_sum == []:
			self.list_of_num_sum.append(sum(self.list_numbers[:3]))
		self.list_of_num_sum.append(sum(self.list_numbers[-3:]))


	def contains(self, total):
		"""
		:param total: (int) The total to check for.
		:returns: (bool) If MovingTotal contains the total.
		"""
		if total in self.list_of_num_sum:
			return True
		else:
			return False


if __name__ == "__main__":
	movingtotal = MovingTotal()

	movingtotal.append([1, 2, 3, 4])
	print(movingtotal.contains(6))
	print(movingtotal.contains(9))
	print(movingtotal.contains(12))
	print(movingtotal.contains(7))

	movingtotal.append([5])
	print(movingtotal.contains(6))
	print(movingtotal.contains(9))
	print(movingtotal.contains(12))
	print(movingtotal.contains(7))
