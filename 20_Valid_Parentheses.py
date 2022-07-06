'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.'''

class Solution:
	def isValid(self, s: str) -> bool:
		my_dict = {
			'(': ')',
			'{': '}',
			'[': ']',
		}

		ss = list(s)
		new_list = []

		def checker():
			while ss != []:
				key = ss[0]
				if key in my_dict and my_dict[key] in ss:
					key_index = ss.index(key)

					value_of_key = my_dict[key]
					value_index = ss.index(value_of_key)

					for n_index, n_ket in enumerate(ss[key_index+1:value_index]):
						if n_ket == key:
							key_index = n_index + 1
					check_list = ss[(key_index+1):value_index]
					del ss[key_index:(value_index + 1)]
					if check_list != []:
						new_list.append(check_list)
				else:
					return False

			if ss == [] and new_list == []:
				return True
			else:
				ss.extend(new_list.pop(0))
				return checker()

		return checker()




s = "()(()"  # True:  {}{{}}  (([]){})     {}[{}] ( ((){})(){} )      {}([{}{}][])[{}]   [{}{}][]
#                        False:   ([)]
sol = Solution()
print(sol.isValid(s))
