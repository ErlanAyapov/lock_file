def read_file(src):
	with open(src, 'r', encoding='utf-8') as file:
		text = file.read()
	with open(src, 'w', encoding='utf-8') as file:
		file.write('')
	return text

def change_file(src, data):
	with open(src, 'a', encoding='utf-8') as file:
		for text in data:
			file.write(text)