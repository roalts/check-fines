from registration_number import check_registraion_number
from api_request import api_requests


def read_reg_num():
    f = open('textfile', 'r+')
    for number in f:
        print number
        number = number.strip('\n')
        reg_num = check_registraion_number(number)
        result = api_requests(reg_num)
        f = open('result_file', 'a')
        if result != "No Fines":
            f.write(number + ": " + result + "\n")
if __name__ == "__main__":
    read_reg_num()
