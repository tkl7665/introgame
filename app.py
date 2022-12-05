import sys
import random
import time

unit_list=['Unit A','Unit B','Unit C','Unit D','Unit E']
captured_units=[]

def print_list(units):
	id=0
	for unit in units:
		id+=1
		print('{0}. {1}'.format(id,unit))
	print()

def option_1():
	print('List of units: ')
	print_list(unit_list)

	try:
		choice=int(input('Your choice: '))-1
		print()

		if choice>=0 and choice<len(unit_list):
			print('{0} selected'.format(unit_list[choice]))
			print('Rolling dice')

			for i in range(5):
				print('.')
				time.sleep(1)

			dice_roll=random.randint(1,6)
			print('{0} rolled!'.format(dice_roll))

			if dice_roll%2==0:
				print('Success!')
				captured_units.append(unit_list[choice])
			else:
				print('Failed!')
		else:
			raise ValueError	

	except ValueError:
		print('Invalid choice. Integers only')
		print()

def option_2():
	count=len(captured_units)
	if count>0:
		print('Number Units recruited [{0}]'.format(count))
		print_list(captured_units)

		print('TO DO: how can you select a unit and have an action with it')
	else:
		print('None Captured!')

def start_game():
	quit=False

	while not quit:
		print('1. Capture a unit')
		print('2. List captured unit(s)')
		print('9. Quit')
		print()

		try:
			choice=int(input('Your choice: '))
			print()

			if choice==1:
				option_1()
			elif choice==2:
				option_2()
			elif choice==9:
				print('Bye')
				quit=True
			else:
				print('Option not availale.')
			print()

		except ValueError:
			print('Invalid choice. Integers only.')
			print()

print()
print('   ___________  ')
print('  /           \\  ')
print(' |     /**     | ')
print('  \\    \\*     /  ')
print('   \\    *\\   /   ')
print('    \\  **/  /    ')
print('     \\     /     ')
print('      \\   /      ')
print('       \\_/      ')
print()

print('Your First Game')
print('-------------------')
print('You define what you want to do here')

print()
start_game()

'''
1. Changing the names of the units
2. Changing the name of the options
3. Counting the success rate of capturing a unit
4. Changing the odds of getting a unit
5. Changing the duration of a dice roll
6. Adding the option of doing something with a unit
7. Releasing a unit
8. Saving and loading the state of the game
'''