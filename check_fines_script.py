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
        result = []
        if len(j) > 0:
            print len(j)
            for i in range(len(j)):
                print i
                result.append("Offence = " + j[i].get('OFFENCE') + " Amount = " + j[i].get('AMOUNT'))
                print result[i]
            return result
        else:
            result.append("No Fines")
            print result[0]
            return result


def check_registration_number(reg_num):
    reg_num_dict = {}
    if 9 <= len(reg_num) <= 10:
        reg_num1 = reg_num[0] + reg_num[1]
        reg_num2 = reg_num[2] + reg_num[3]
        reg_num4 = reg_num[-4:]
        reg_num3 = reg_num[4] if len(reg_num) == 9 else reg_num[4] + reg_num[5]
        if reg_num1 == "KA" and reg_num4.isdigit() and (0 <= int(reg_num2) <= 99):
            reg_num_dict[1] = reg_num1
            reg_num_dict[4] = reg_num4
            reg_num_dict[2] = reg_num2
            if reg_num3.isalpha():
                reg_num_dict[3] = reg_num3
                print reg_num_dict[1], reg_num_dict[2], reg_num_dict[3], reg_num_dict[4]
                print "true"
                return reg_num_dict
            else:
                print "false4"
                return None
        else:
            print "false"
            return None

    else:
        print "Invalid Registration Number"
        return None


def read_reg_num():
    f = open('textfile', 'r+')
    for number in f:
        print number
        number = number.strip('\n')
        reg_num = check_registration_number(number)
        result = api_requests(reg_num)
        f = open('result_file', 'a')
        if result[0] != "No Fines":
            fine = "fines\n" if len(result) > 1 else "fine\n"
            f.write(number + " has " + str(len(result)) + fine)
            for i in result:
                f.write(number + ": " + i + "\n")

if __name__ == "__main__":
    read_reg_num()
