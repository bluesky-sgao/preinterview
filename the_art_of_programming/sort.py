def insertion_sort(s):
    if len(s) == 1:
        return s
    for i in xrange(1, len(s)):
        temp = s[i]
        j = i - 1
        while(j >= 0 and temp < s[j]):
#         while(j >= 0 and temp > s[j]):
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = temp
    print s

def my_merge_sort(s):
    num_s = len(s)
    if num_s <= 1:
        return s
    s_1 = s[:num_s / 2]
    s_2 = s[num_s / 2:]
    left = my_merge_sort(s_1)
    right = my_merge_sort(s_2)
    return merge(left, right)

def merge(s_1, s_2):
    num_1 = len(s_1)
    num_2 = len(s_2)
    merged = []
    i = 0
    j = 0
    while (i < num_1 and j < num_2):
            if s_1[i] >= s_2[j]:
                merged.append(s_2[j])
                j += 1
            else:
                merged.append(s_1[i])
                i += 1
    while i < num_1:
        merged.append(s_1[i])
        i += 1
    while j < num_2:
        merged.append(s_2[j])
        j += 1
    return merged

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
 
    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        return merged
 
    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

if __name__ == "__main__":
    string_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    string_2 = ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
    string_3 = ["j", "i", "h", "a"]
#     print "a" < "b"
#     print range(3)
#     print xrange(1, 3).__len__()
#     insertion_sort(string_1)
#     insertion_sort(string_2)
#     s_1 = ["a", "c", "e"]
#     s_2 = ["b", "d", "f"]
#     merge(s_1, s_2)
#     print merge_sort(string_3)
    print my_merge_sort(string_2)
