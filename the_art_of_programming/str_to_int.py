def str_to_int_right_scan(s):
    num_s = len(s)
    result = 0
    for i in range(num_s):
        result += int(s[num_s - 1 - i]) * pow(10, i)
    return result

def str_to_int_left_scan(s):
    num_s = len(s)
    result = 0
    for i in range(num_s):
        result = result * 10 + int(s[i])
    return result

def str_to_int_left_scan_owerflow(s):
    num_s = len(s)
    result = 0
    for i in range(num_s):
        result = result * 10 + int(s[i])
    return result

if __name__ == "__main__":
    string = ["1", "2", "3", "4"]
    string_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     print str_to_int_right_scan(string)
#     print str_to_int_left_scan(string)
    print str_to_int_right_scan(string_1)
    print str_to_int_left_scan(string_1)