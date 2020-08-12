#  A string of the the one keystroke characters.
ones = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ "

# A string of the two keystroke characters.
twos = "~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"

# Use zip to create a dictionary one and two keystroke characters.
ones_dict = dict(zip(ones, [1 for i in range(len(ones))]))
twos_dict = dict(zip(twos, [2 for i in range(len(ones))]))

# Combine the two dictionaries into one.
big_dict = {}
big_dict.update(ones_dict)
big_dict.update(twos_dict)

def num_key_strokes(text):
	sum = 0
	for c in text:
		sum += big_dict[c]
	return sum

# A test string.	
t = "0297350298-02-30856-174346"
print(f'The number of keystrokes in {t} is {num_key_strokes(t)}')