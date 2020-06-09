from collections import Counter

def get_strings(city):
	city = city.lower()
	letters = Counter(city)
	list1 = []
	for item in letters:
		if item.isalpha():
			let, count = item, letters[item]
			ast = '*'*count
			list1.append(f'{let}:{ast}')
	return ','.join(list1)

print(get_strings('Las Vegas'))
