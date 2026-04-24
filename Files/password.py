import time

system = 0
locked = 0

while True:
	pw = input("please enter password\n")
	if pw == '123456':
		print('system opened.\n')
		system += 1
		break
	elif pw == 'exit' or locked >= 5:
		print('system closed.')
		break
	else:
		print('ERROR!')
		locked += 1
if system == 1:
	time.sleep(0.5)
	print('welcome to SCP foundation!\n')
		
		