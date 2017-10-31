import urllib2
import json


def api_requests(reg_num):
    if registration_number is None:
        print "Invalid Registration Number"
    else:
        url = "http://btpsmartphone.appspot.com/btpfines?appversioncode=34&txtNewReg1=" + registration_number[1] + "&txtNewReg2=" + \
              registration_number[2] + "&txtNewReg3=" + registration_number[3] + "&txtNewReg4=" + registration_number[4]
        response = urllib2.urlopen(url)
        html = response.read()
        # html = json.dumps(response.read())
        offence_details = json.loads(html)
        if len(j) > 0:
            result = "Offence = " + offence_details[0].get('OFFENCE') + " Amount = " + offence_details[0].get('AMOUNT')
            print result
            return result
        else:
            result = "No Fines"
            print result
            return result
