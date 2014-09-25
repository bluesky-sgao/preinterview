import sys

def is_palindrome(s):
    num_s = len(s)
    for i in range(num_s / 2):
        if s[i] != s[num_s - 1 - i]:
            print "FAIL"
            sys.exit()
    print "PASS"

if __name__ == "__main__":
    s_1 = ["a", "b", "c", "b", "a"]
    s_2 = ["a", "b", "c", "a", "b"]
    is_palindrome(s_1)
    is_palindrome(s_2)
