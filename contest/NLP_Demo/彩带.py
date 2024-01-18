def get_longest_substring(s, k):
    n = len(s)
    freq = {}
    left, right = 0, 0
    max_len = 0

    while right < n:
        if s[right] not in freq:
            freq[s[right]] = 0
        freq[s[right]] += 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right-left+1)
        right += 1

    return max_len

N, K = map(int, input().split())
List = list(map(int, input().split()))
s = ""
for i in List:
    s += str(i)

print(get_longest_substring(s, K))
