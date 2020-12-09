import re
#
# amounts = r"thousand|million|billion"
# number = r"\d+(,\d{3})*\.*\d*"
# standard = fr"\${number}(-|\sto\s)?({number})?\s({amounts})"
#
# def word_to_value(word):
# 	value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
# 	return value_dict.get(word.lower(), 1)
#
# def parse_word_syntax(string):
# 	stripped_string = string.replace(",", "")
# 	value = float(re.search(number, stripped_string).group())
# 	modifier = word_to_value(re.search(amounts, string, flags=re.I).group())
# 	return value*modifier
#
# def parse_value_syntax(string):
# 	stripped_string = string.replace(",", "")
# 	return float(re.search(number, stripped_string).group())
#
# def money_conversion(money):
# 	if type(money) == list:
# 		money = money[0]
#
# 	word_syntax = re.search(standard, money, flags=re.I)
# 	value_syntax = re.search(fr"\${number}", money)
#
# 	if word_syntax:
# 		return parse_word_syntax(word_syntax.group())
# 	elif value_syntax:
# 		return parse_value_syntax(value_syntax.group())
# 	else:
# 		return None

def word_to_value(word):
	value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
	return value_dict.get(word.lower(), 1)


def money_conversion(string):
	if type(string) == list:
		string = string[0]
	if string == 'N/A':
		return None

	if string != None:
		amount = re.search(r'thousand|million|billion', string, re.I)
		amount
	try:
		if amount == None:
			num = re.search(r'(?<=\$)?\s?(\d+)\.?(?:\,)?(\d+)?(?:\,)?(\d+)?', string)
			li = [i for i in num.groups() if i != None]
			final_val = ''.join(li)
			final_val = float(final_val)
			return final_val
		elif amount.group() == 'million' or amount.group() == 'billion' or amount.group() == 'thousand':
			num = re.search(r'(?<=\$)?\s?(\d+)\.?(?:\,)?(\d+)?(?:\,)?(\d+)?', string)
			li = [i for i in num.groups() if i != None]
			n = '.'.join(li)
			n = float(n)
			modifier = word_to_value(amount.group())
			final_val = n * modifier
			return final_val
		else:
			return None
	except Exception as e:
		print(string)
		print(e)

print(money_conversion('$3 million'))