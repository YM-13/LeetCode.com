import json


def make_and_sort_value(data, value):
	'''func returns sorted value of dictionaris by name or price'''
	list_of_value = []  # a list with value from dictionaries in a list by a given key
	for dict in data:  # data = list_with_incoming_dicts
		list_of_value.append(dict[value])  # value  = "name" or "price"
	list_of_value.sort()
	return list_of_value


def append_func(data, key, value_of_key):
	'''func returns a list with dictionaries that have the given key'''
	new_list_with_dicts = []
	for dict in data:
		if value_of_key == dict[key]:
			new_list_with_dicts.append(dict)
	return new_list_with_dicts


def sort_by_price_ascending(json_string):
	list_with_incoming_dicts = json.loads(json_string)

	new_list_with_dicts = []

	list_of_prices = make_and_sort_value(list_with_incoming_dicts, "price")
	price_c = -1
	for price in list_of_prices:

		if price != price_c:
			price_c = price

			if list_of_prices.count(price) == 1:
				new_list_with_dicts = append_func(list_with_incoming_dicts, 'price', price)
			else:
				time_list_of_dicts = append_func(list_with_incoming_dicts, 'price', price)
				list_of_names = make_and_sort_value(time_list_of_dicts, "name")

				for name in list_of_names:
					t = append_func(time_list_of_dicts, 'name', name)
					new_list_with_dicts.append(t)

				time_list_of_dicts.clear()

	return json.dumps(new_list_with_dicts)


print(sort_by_price_ascending(
	'[{"name":"smuzzz","price":9.99}, {"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
