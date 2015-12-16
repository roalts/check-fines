import urllib2
import json


def api_requests(reg_num):
    if reg_num is None:
        print "Invalid Registration Number"
    else:
        url = "http://btpsmartphone.appspot.com/btpfines?appversioncode=34&txtNewReg1=" + reg_num[1] + "&txtNewReg2=" + \
              reg_num[2] + "&txtNewReg3=" + reg_num[3] + "&txtNewReg4=" + reg_num[4]
        response = urllib2.urlopen(url)
        html = response.read()
        # html = json.dumps(response.read())
        j = json.loads(html)
        if len(j) > 0:
            result = "Offence = " + j[0].get('OFFENCE') + " Amount = " + j[0].get('AMOUNT')
            print result
            return result
        else:
            result = "No Fines"
            print result
            return result
