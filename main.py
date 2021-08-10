from keys import get_secret
import menu

def display_data(data):
	print('Password: ', data[0])
	print('Username: ', data[1])
	print('Email: ', data[2])
	print('Url: ', data[3])
	print('Website: ', data[4], '\n')

def main():
	secret = get_secret()
	input_secret = input('Please type master password: ')

	if input_secret == secret:
		print('You\'re in :)')
	else:
		print('Sorry, no luck :(')
		exit()

	print('-' * 5, 'Welcome', '-' * 5)

	finish = False
	while not finish:

		selection = menu.get_main_menu()

		if selection == '1':
			# Add new password
			result = menu.add_new_pwd(input_secret)
			if result:
				print('\nAdded: ')
				display_data(result)
			else:
				print('Error: not retrieving data from db')

		elif selection == 'Q' or selection == 'q':
			print('Goodbye.')
			finish = True

		else:
			print('You didn\'t select a correct option')


if __name__ == '__main__':
	main()