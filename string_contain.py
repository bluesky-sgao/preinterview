import sys

def string_contain(s_1, s_2):
    num_1 = len(s_1)
    num_2 = len(s_2)
    for j in range(num_2):
        for i in range(num_1):
            if s_2[j] == s_1[i]:
                print "MATCHED: %s" % s_2[j]
                break
            else:
                if i == num_1 - 1:
                    print "FAIL"
                    sys.exit()
    print "PASS"



if __name__ == "__main__":
    string_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    string_2 = ["a", "b", "c"]
    string_3 = ["a", "b", "k"]
#     shift_char(string, 3)
#     shift_char_2(string, 4)
#     reverse(string, 2, 10)
    string_contain(string_1, string_2)
    string_contain(string_1, string_3)
