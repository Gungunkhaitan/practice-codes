def longest_common_subsequence(s1, s2):
 m, n = len(s1), len(s2)
 dp = [[0] * (n + 1) for _ in range(m + 1)]
 for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs_length = dp[m][n]
 lcs = []
 while m > 0 and n > 0:
    if s1[m - 1] == s2[n - 1]:
        lcs.append(s1[m - 1])
        m -= 1
        n -= 1
    elif dp[m - 1][n] > dp[m][n - 1]:
        m -= 1
    else:
        n -= 1
 lcs.reverse() 
 return ''.join(lcs), lcs_length
s1 = "Gungunkhaigun"
s2 = "Khaitangunian"
lcs, length = longest_common_subsequence(s1, s2)
print(f"Longest Common Subsequence: {lcs}\n Length: {length}")
