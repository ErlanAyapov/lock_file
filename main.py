from sys import argv
from settings import get_command
from random import randint
from time import sleep


def main():   
	get_command()
	for _ in range(100):
		print( randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1),)
		sleep(0.01)
	print('\n====================================================================\nЖоба оқу үйрену мақсатында жасалған, автор іс әрекеттеріңізге жауапты емес!')
	print('Сәтті аяқталды\n====================================================================')

if __name__ == '__main__':
	main()

# Жоба оқу үйрену мақсатында жасалған, автор іс әрекеттеріңізге жауапты емес!