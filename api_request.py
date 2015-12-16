import urllib2
import json

def api_requests(regNum):
	if regNum == None:
		print "Invalid Registration Number"
	else:
		url = "http://btpsmartphone.appspot.com/btpfines?appversioncode=34&txtNewReg1="+regNum[1]+"&txtNewReg2="+regNum[2]+"&txtNewReg3="+regNum[3]+"&txtNewReg4="+regNum[4]
		response = urllib2.urlopen(url)
		html = response.read()
		# html = json.dumps(response.read())
		j = json.loads(html)
		if len(j) > 0:
			print "Offence = " + j[0].get('OFFENCE') + " Amount = " + j[0].get('AMOUNT')
		else:
			print "No Fines"

		