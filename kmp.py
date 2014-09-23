# Knuth-Morris-Pratt
import sys

def violent_match_1(s, p):
    num_s = len(s)
    num_p = len(p)
    for i in range(num_s - num_p):
        print "i = %s" % i
        for j in range(num_p):
            print "j = %s" % j
            if s[i + j] == p[j]:
                if j == num_p - 1:
                    print "PASSED"
                    print i
                    sys.exit()
                continue
            else:
                break

def violent_match_2(s, p):
    num_s = len(s)
    num_p = len(p)
    i = 0
    j = 0
    while (i < num_s and j < num_p):
        print "i = %s" % i
        print "j = %s" % j
        if (s[i] == p[j]):
            i = i + 1
            j = j + 1
        else:
            i = i - j + 1
            j = 0
    if j == num_p:
        print "PASSED"
        print i - j
    else:
        print "FAILED"

def get_next(p):
    num_p = len(p)
    next = []
    next.append(-1)
    k = -1
    j = 0
    while(j < num_p - 1):
        if (k == -1 or p[j] == p[k]):
            k = k + 1
            j = j + 1
#             next[j] = k
            next.append(k)
        else:
            k = next[k]
    print "next: %s" % next
    return next

def get_next_2(p):
    num_p = len(p)
    next = []
    next.append(-1)
    k = -1
    j = 0
    while(j < num_p - 1):
        if (k == -1 or p[j] == p[k]):
            k = k + 1
            j = j + 1
            if (p[j] != p[k]):
                next.append(k)
            else:
                # can not be p[j]=p[next[j]], so k=next[k]=next[next[k]]
                # next[j] = next[k]
                next.append(next[k])
        else:
            k = next[k]
    print "next: %s" % next
    return next

def kmp_match(s, p, next):
    i = 0
    j = 0
    num_s = len(s)
    num_p = len(p)
    while (i < num_s and j < num_p):
        print "i = %s" % i
        print "j = %s" % j
        if (j == -1 or s[i] == p[j]):
            i = i + 1
            j = j + 1
        else:
            j = next[j]
    if j == num_p:
        print "PASSED"
        print i - j
    else:
        print "FAILED"

if __name__ == "__main__":
    s = ["a", "b", "c", "d", "e", "f", "g", "h", "a", "b", "a", "b", "c", "d"]
    p = ["a", "b", "c", "d", "e"]
    p_1 = ["a", "b", "a"]
#     violent_match_1(s, p)
#     violent_match_2(s, p)
#     print get_next(p)
#     print get_next_2(p)
    kmp_match(s, p, get_next(p))
    kmp_match(s, p_1, get_next(p))
