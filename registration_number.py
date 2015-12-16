def check_registraion_number(registraionNumber):
	'''(string) -> list
	checks if the registration number is valid or not'''
	regNum = {}
	if len(registraionNumber) >= 9 and len(registraionNumber) <=10:
		regNum1 = registraionNumber[0] + registraionNumber[1]
		regNum2 = registraionNumber[2] + registraionNumber[3]
		regNum4 = registraionNumber[-4:]
		regNum3 = registraionNumber[4] if len(registraionNumber) == 9 else registraionNumber[4] + registraionNumber[5]
		if regNum1 == "KA" and regNum4.isdigit() and (int(regNum2) >= 0 and int(regNum2) <= 99):
			regNum[1] = regNum1
			regNum[4] = regNum4
			regNum[2] = regNum2
			if regNum3.isalpha():
				regNum[3] = regNum3
				print regNum[1], regNum[2], regNum[3], regNum[4]
				print "true"
				return regNum
			else:
				return None
				print "false4"
		else:
			return None
			print "false"
	else:
		return None
		print "Invalid Registration Number"
