'''
	Name: Shopping Cart
	Author: Eric Stalcup
	Created: 1/26/2023
'''

# Display's the main menu, return user input
def main_menu():
	print('----MAIN MENU----')
	print('s: Shop')
	print('x: Exit')
	option = input('Option: ').lower()
	while not (option == 'x' or option == 's'):
		option = input('Invalid (s/x): ')
	return option

# Display shopping cart items, return user input
def cart_menu():
	print('----CART MENU----')
	print('1: Cookie - $1.50')
	print('2: Sandwich - $4.00')
	print('3: Water - $1.00')
	item = input('Item: ')
	while not (item == '1' or item == '2' or item == '3'):
		item = input('Invalid (1-3): ')
	
	item_name = ''
	item_price = 0.00

	if item == '1':
		item_name = 'cookie'
		item_price = 1.50
	elif item == '2':
		item_name = 'sandwich'
		item_price = 4.00
	elif item == '3':
		item_name = 'water'
		item_price = 1.00
	
	return item_name, item_price

# Keeps track of item count, total cost, and dispalys final output.
def main():
	cookies = 0
	sandwiches = 0
	waters = 0
	grand_total = 0.00

	option = main_menu()
	while True:
		if option == 's':
			item_name, item_price = cart_menu()
			if item_name == 'cookie':
				cookies += 1
			elif item_name == 'sandwich':
				sandwiches += 1
			elif item_name == 'water':
				waters += 1
			grand_total += item_price

			print('Added', item_name)
			option = main_menu()
		if option == 'x':
			break

	print('--------------------')
	if cookies > 0:
		print(f'({cookies}) - Cookie = ${(cookies * 1.50):.2f}')
	if sandwiches > 0:
		print(f'({sandwiches}) - Sandwich = ${(sandwiches * 4.00):.2f}')
	if waters > 0:
		print(f'({waters}) - Water = ${(waters * 1.00):.2f}')
	print('--------------------')
	print(f'GRAND TOTAL = ${grand_total:.2f}')
	print('--------------------')

main()
