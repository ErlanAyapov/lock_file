from hash import un_hashing, hashing

def get_command():
	method_type = input('Шифрлау / шифрды ашу | 0/1: ')
	object_src = input('Файлға дейінгі толық мекенжай:\nМысалы: "C:/Users/Ерлан/Desktop/mob.txt"\nФайлға мекенжай: ')
	object_key = int( input('Шифр коды: ') )
	if method_type == '0':
		hashing(object_key, object_src) 
	elif method_type == '1':
		un_hashing(object_key, object_src) 