import getpass
import string
import os
users = ['sparsh', 'dhanveer', 'amlaan','ram', 'pramukh']
pins = ['1234', '2345', '3456','4567','5678']
amounts = [1000, 2000, 3000,5000,10000]
count = 0
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		elif user == users[2]:
			n = 2
		elif user == users[3]:
			n = 3
		else:
			n = 4
		break
	else:
		print('INVALID USERNAME')
while count < 5:
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	if pin.isdigit():
		if user == 'sparsh':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()

		if user == 'dhanveer':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
				
		if user == 'amlaan':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
		if user == 'ram':
			if pin == pins[3]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
		if user == 'pramukh':
			if pin == pins[4]:
				break
			else:
				count += 1
				print('INVALID PIN')
				print()
	else:
		print('PIN CONSISTS OF 4 DIGITS')
		count += 1
	
if count == 5:
	print('5 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	exit()

print('LOGIN SUCCESFUL, CONTINUE')

print()

print(str.capitalize(users[n]), 'welcome to ATM')

print('----------ATM SYSTEM-----------')
while True:
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement_(S) \nWithdraw_(W) \nChange PIN(P)  \nQuit___(Q) \n: ').lower()
	valid_responses = ['s', 'w','p', 'q']
	response = response.lower()
	if response == 's':
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'RUPEES ON YOUR ACCOUNT.')
		
	elif response == 'w':
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		if cash_out%100 != 0:
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100 RUPEE NOTES')
		elif cash_out > amounts[n]:
			print('YOU HAVE INSUFFICIENT BALANCE')
		else:
			amounts[n] = amounts[n] - cash_out
			print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEE')

	elif response == 'p':
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			if new_ppin != new_pin:
				print('PIN MISMATCH')
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
	elif response == 'q':
	    print('THANKYOU FOR BANKING WITH US')
	    exit()
	else:
		print('RESPONSE NOT VALID')
