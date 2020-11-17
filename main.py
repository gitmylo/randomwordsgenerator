from databasey import combinedlist
import random

running = True
amount = 0
amount = int(input('how many words?: '))
while running:
	word = ""
	for i in range(amount):
		word += random.choice(combinedlist)
	print(word)
	wantsexit = input("type 'x' to exit: ")
	if wantsexit == 'x':
		running = False