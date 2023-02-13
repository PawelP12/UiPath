import re
def validate_input(input_city):
	if re.fullmatch("^[a-zA-Z-\s]+$",input_city):
		return "Valid"
	else:
		return "Incorrect"



