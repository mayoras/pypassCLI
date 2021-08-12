import re

def isEmail(emailOrUsername):
	isEmail = False
	pattern_email = "^(?:(?!.*?[.]{2})[a-zA-Z0-9](?:[a-zA-Z0-9.+!%-]{1,64}|)|\"[a-zA-Z0-9.+!% -]{1,64}\")@[a-zA-Z0-9][a-zA-Z0-9.-]+(.[a-z]{2,}|.[0-9]{1,})$"

	if re.search(pattern_email, emailOrUsername):
		isEmail = True
	return isEmail