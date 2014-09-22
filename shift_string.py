# method 1
def shift_first_char(s):
    num = len(s)
    temp = s[0]
    for i in range(num - 1):
        s[i] = s[i + 1]
    s[num - 1] = temp

def shift_char(s, n):
    for i in range(n):
        shift_first_char(s)
    print s
# method 2
def shift_char_2(s, n):
    num = len(s)
    temp = []
    for i in range(n):
        temp.append(s[i])
    for i in range(num - n):
        s[i] = s[i + n]
    for i in range(n):
        s.append(temp[i])
    print s
# method 3
def reverse(s, begin, end):
    num = end - begin
    for i in range(num / 2):
        temp = s[begin + i]
        s[begin + i] = s[end - 1 - i]
        s[end - 1 - i] = temp
#     print s

def three_step_rotate(s, n):
    num = len(s)
# it will generate new list, can not satisfy
#     reverse(s[0:n])
#     reverse(s[n + 1:num])
    reverse(s, 0, n)
    reverse(s, n, num)
    reverse(s, 0, num)
    print s

if __name__ == "__main__":
    string = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#     shift_char(string, 3)
#     shift_char_2(string, 4)
#     reverse(string, 2, 10)
    three_step_rotate(string, 5)
