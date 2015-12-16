def check_registraion_number(reg_num):
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
