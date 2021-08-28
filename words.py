def words_to_sentence(words):
	return ' '.join(words)

lst = ['The', 'boy', 'runs.']
sent = words_to_sentence(lst)
print(f'The sentence "{sent}" has length {len(sent)}.')