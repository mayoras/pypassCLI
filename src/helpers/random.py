import random, string

def gen_random_str(size):
	# Random string will always be an ASCII-char string
	chars = string.ascii_letters + string.punctuation
	return "".join(random.choice(chars) for x in range(size))