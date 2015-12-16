def check_registraion_number(registraionNumber):
	'''(string) -> list
	checks if the registration number is valid or not'''
	regNum = {}
	if len(registraionNumber) >= 9 and len(registraionNumber) <=10:
		regNum1 = registraionNumber[0] + registraionNumber[1]
		if regNum1 == "KA":
			regNum[1] = regNum1
			regNum2 = registraionNumber[2] + registraionNumber[3]
			if int(regNum2) >= 0 and int(regNum2) <= 99:
				regNum[2] = regNum2
				if len(registraionNumber) == 9:
					regNum3 = registraionNumber[4]
				else:
					regNum3 = registraionNumber[4] + registraionNumber[5]
				regNum[3] = regNum3
				if regNum3.isalpha():
					regNum4 = registraionNumber[-4:]
					if regNum4.isdigit():
						regNum[4] = regNum4
						return regNum
						print "true"
					else:
						return None
						print "false4"
				else:
					return None
					print "false3"
			else:
				return None
				print "false2"
		else:
			return None
			print "false"
	else:
		return None
		print "Invalid Registration Number"