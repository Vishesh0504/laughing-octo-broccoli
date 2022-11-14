import random

computer = ['paper' , 'stone' , "scissors" ]
computer_choice=random.choice(computer)


num_games=int(input('Number of times you want to play'))
for i in range(num_games):
	score=0
	while True:
		user_input=input('Enter you choice:')
		user_choice=user_input.lower()
		if user_choice in computer:
			break 
		else:
			print('Invalid input')
			continue
	computer = ['paper' , 'stone' , "scissors" ]
	computer_choice=random.choice(computer)
	print(computer_choice)

	if user_choice=='end':
		print('Thank you for playing')
		break
	if user_choice=='scissors' and computer_choice=='paper':
		print('you won')
		score+=1
	elif user_choice=='scissors' and computer_choice=='stone':
		print('you lost')
	elif user_choice=='scissors' and computer_choice=='scissors':		
		print('tied')
	elif user_choice=='paper' and computer_choice=='stone':	
		print('you won')
		score+=1
	elif user_choice=='paper' and computer_choice=='scissors':	
		print('you lost')
	elif user_choice=='paper' and computer_choice=='paper':	
		print('tied')
	elif user_choice=='stone' and computer_choice=='scissors':
		print('you won')
		score+=1
	elif user_choice=='stone' and computer_choice=='paper':
		print('you lost')
	elif user_choice=='stone' and computer_choice=='stone':
		print('tied')
	print(score)					
