import requests  # for API request
import hashlib
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	response = requests.get(url)  # The response object
	if response.status_code != 200:
		raise RuntimeError(f'Error fetching: {response.status_code}, check the API and try again')
	return response

def get_password_leaks_count(data_set, suffix_to_check):
	data_pairs = [line.split(':') for line in data_set.text.splitlines()]  # A generator object of [suffix, count]
	for suffix, count in data_pairs:
		if suffix == suffix_to_check:
			return count
	return 0  # No leak has been found

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  # Hashing the password to SHA1
	first_5_chars, suffix = sha1password[:5], sha1password[5:]
	response = request_api_data(first_5_chars)  # List with suffix of every hash beginning with the specified prefix ('first_5_chars'), followed by a count of how many times it appears in the data set
	return get_password_leaks_count(response, suffix)

def main(args):
	# Option 1
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times')
		else:
			print(f'{password} was NOT found')
	########################

	# # Option 2 (more secure)
	# with open('passwords_input.txt') as f:
	# 	for line in f:
	# 		for password in line.split():
	# 			count = pwned_api_check(password)
	# 			if count:
	# 				print(f'{password} was found {count} times')
	# 			else:
	# 				print(f'{password} was NOT found')
	# ########################

# Will run if it's the main file, and will not run if it's beeing imported
if __name__ == '__main__':
	main(sys.argv[1:])
