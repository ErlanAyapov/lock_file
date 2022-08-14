from file_sets import read_file, change_file
from string import printable


'''
	============================================
	||	Бұл функция файлды шифрлайды 		  ||
	||	шифрлау символдардың индексін		  ||
	||	жылжыту арқылы жүзеге асады			  ||
	||	мысалы шифрлау кілтіне 10 саны 		  ||
	||	енгізілсе онда индекс 10 сан жылжиды  ||
	||	толық ақпарат whatsapp: +7(747)8160485||
	============================================
'''

def hashing(key, src):

	# шифрлау функциясы

	new_word = list() 
	word = read_file(src)
	for i in word:
		try: 
			object_index = printable.index(i) 
			new_word.append( printable[object_index + key] )
		except IndexError:
			object_index = printable.index(i) 
			new_word.append( printable[(object_index + key) - len(printable)] )
	change_file(src, new_word)

def un_hashing(key, src):

	# шифрды ашу функциясы

	un_hushed = list() 
	hushed_text = read_file(src)
	for i in hushed_text:
		try: 
			object_index = printable.index(i) 
			un_hushed.append( printable[object_index - key] )
		except IndexError:
			object_index = printable.index(i) 
			un_hushed.append( printable[(object_index - key) + len(printable)] ) 
	change_file(src, un_hushed)
