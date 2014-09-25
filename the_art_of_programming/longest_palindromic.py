def my_longest_palindrome(s):
    num_s = len(s)
    for i in xrange(1, num_s - 1):
        j = i
        k = i
        while j > 0 and k < num_s - 1:
            if s[j - 1] == s[k + 1]:
                print "palindrome start from: %s, length: %s" % (i, i - j + 1)
                j -= 1
                k += 1
            else:
                break
        j = i
        k = i
        while j > 0 and k < num_s - 1:
            if s[k] == s[j - 1]:
                print "palindrome start from: %s, length: %s" % (i, i - j + 1)
                j -= 1
                k += 1
            else:
                break

def longest_palindrome(s):
    num_s = len(s)
    max = 0
    for i in range(num_s):
        j = 0
        while(i - j >= 0 and i + j < num_s):
            if s[i - j] != s[i + j]:
                break
            j += 1
            temp = j * 2 - 1
        if temp > max:
            max = temp
        j = 0
        while(i - j >= 0 and i + j + 1 < num_s):
            if s[i - j] != s[i + j + 1]:
                break
            j += 1
            temp = j * 2
        if temp > max:
            max = temp
    print max

# def longest_palindrome_inject(s):
#     num_s = len(s)
#     for i in range(num_s):
#         s.insert(i, "#")
#     max = 0
#     p = []
#     num_s_1 = len(s)
#     for i in range(num_s_1):
#         p[i] = max > i?min(p[2 * id - i], max - i):1
#         while(s[i + p[i]]) == s[i - p[i]]
#             p[i] += 1
#         if (i + p[i] > max):
#             max = i + p[i]
#             id = i
#     print max

if __name__ == "__main__":
    s_1 = ["a", "b", "c", "b", "a", "d", "e", "f", "e"]
    s_2 = ["a", "b", "b", "a", "d", "e", "f", "e"]
    s_3 = ["a", "b", "c", "c", "b", "a", "d", "e", "f", "e"]
    longest_palindrome(s_1)
    longest_palindrome(s_2)
#     longest_palindrome_inject(s_1)
#     longest_palindrome_inject(s_2)
#     longest_palindrome_inject(s_3)
