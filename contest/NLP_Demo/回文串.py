def make_palindrome(s):
    n = len(s)
    left, right = 0, n-1
    diff_left, diff_right = -1, -1

    # 找到第一个不同的字符串和最后一个不同的字符
    while left < right:
        if s[left] != s[right]:
            diff_left, diff_right= left, right
            break
        left += 1
        right -= 1

    # 字符串本身就是回文串
    if diff_left == -1:
        return s

    # 不同字符个数大于2
    if diff_left - diff_right >= 1:
        return "impossible"

    # 只有一个不同字符
    if diff_right - diff_left == 0:
        if s[left + 1] == s[right]:
            s = s[:left] + s[left] + s[left+1:] + s[right+1:]
            return s
        elif s[left] == s[right-1]:
            s = s[:right-1] + s[left] + s[right:]
            return s
        else:
            return "impossible"

    # 有两个不同的字符
    if s[diff_left+1] == s[diff_right]:
        s = s[:diff_left] + s[diff_right] + s[diff_left+1:] + s[diff_right+1:]
    elif s[diff_left] == s[diff_right]:
        s = s[:diff_right-1] + s[diff_left] + s[diff_right:]
    else:
        return "impossible"

    # 检查修改后的字符串是否返回回文串
    if s != s[::-1]:
        return "impossible"

    return s


s1 = str(input())
print(make_palindrome(s1))
