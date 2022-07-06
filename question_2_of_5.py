"""The CropRatio object can be used to calculate what proportion of a farm's harvest is a specific crop.
The object's proportion method should return 0 for crops that were not added."""


class CorpRatio:

	def __init__(self):
		self._crops = {}
		self._total_weight = 0

	def add(self, name, crop_weight):

		if not name in self._crops:
			self._crops[name] = crop_weight
		else:
			#curr_crop_weight = self._crops[name]
			self._crops[name] = self._crops[name] + crop_weight

		self._total_weight += crop_weight

	def proportion(self, name):

		if name in self._crops:
			return self._crops[name] / self._total_weight
		else:
			return 0


if __name__ == "__main__":
	crop_ratio = CorpRatio()
	crop_ratio.add('Wheat', 4)
	crop_ratio.add('Wheat', 5)
	crop_ratio.add('Rice', 1)

	print((crop_ratio.proportion('Wheat')))
	print((crop_ratio.proportion('Raps')))
	print((crop_ratio.proportion('Rice')))
