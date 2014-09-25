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

def string_contain_sort(s_1, s_2):
    import sort
    s1 = sort.my_merge_sort(s_1)
    s2 = sort.my_merge_sort(s_2)
    num_1 = len(s1)
    num_2 = len(s2)
    i = 0
    j = 0
    while (i < num_1 and j < num_2):
            if s_2[j] == s_1[i]:
                print "MATCHED: %s" % s_2[j]
                j += 1
            else:
                i += 1
    if i == num_1:
        print "FAIL"
        sys.exit()
    print "PASS"

def string_contain_prime(s_1, s_2):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101];
    print ord("a"), ord("b")
    num_1 = len(s_1)
    num_2 = len(s_2)
    devidend = 1
    for i in range(num_1):
        temp = prime[ord(s_1[i]) - 97]
        if devidend % temp != 0:
            devidend = devidend * temp
    for j in range(num_2):
        temp = prime[ord(s_2[j]) - 97]
        if devidend % temp != 0:
            print "FAIL"
            sys.exit()
    print "PASS"

def string_contain_hash(s_1, s_2):
    num_1 = len(s_1)
    num_2 = len(s_2)
    py_hash = set()
    for i in range(num_1):
        py_hash.add(s_1[i])
    for j in range(num_2):
        if s_2[j] not in py_hash:
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
#     string_contain(string_1, string_2)
#     string_contain(string_1, string_3)
#     string_contain_sort(string_1, string_2)
#     string_contain_sort(string_1, string_3)
#     string_contain_prime(string_1, string_3)
    string_contain_hash(string_1, string_2)
