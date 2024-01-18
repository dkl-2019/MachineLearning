# 判断是否为回文串
def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    n = len(s)
    mid = n//2

    # 找到第一个不同的字符
    i = 0
    while i < mid and s[i] == s[n-1-i]:
        i += 1

    # 如果s已经是回文
    if i == mid:
        return s

    # 将第一个不同的字符修改为较小的那个
    j = n - i - 1
    s = s[:i] + min(s[i], s[j]) + max(s[i], s[j]) + s[i+1:j] + min(s[i], s[j]) + max(s[i], s[j]) + s[j+1:]

    # 如果该操作使得s变成了回文，则返回
    if is_palindrome(s):
        return s

    # 将倒数第二个不同的字符修改为较小的那个，
    i += 1
    while i < mid and s[i] == s[n-1-i]:
        i += 1
    j = n - i - 1
    return s[:i-1] + min(s[i-1], s[j]) + max(s[i-1], s[j]) + s[i:j] +min(s[i-1], s[j]) + max(s[i-1], s[j]) + s[j+1:]

if __name__ == '__main__':
    s = input().split()
    print(make_palindrome(s)[0])

