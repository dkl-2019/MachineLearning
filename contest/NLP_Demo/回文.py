def min_pelindrome(s: str) -> str:
    s = list(s)
    n = len(s)
    changed = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if changed < 2:
                if s[i] < s[n -i -1]:
                    s[n - i - 1] = s[i]
                else:
                    s[i] = s[n -i - 1]
                changed += 1
            else:
                return "无法在题目限制下行成回文字符串"
    return "".join(s)

s = str(input())
print(min_pelindrome(s))