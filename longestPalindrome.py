def longest_palindrome_dp(X):
    n = len(X)
    Y = X[::-1]
    
    # Initialize DP table
    L = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Fill the table for LCS(X, reverse(X))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L

def reconstruct_lps(L, X):
    i, j = len(X), len(X)
    Y = X[::-1]
    lps = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lps.append(X[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lps))

# Main
X = "character"
L = longest_palindrome_dp(X)
lps = reconstruct_lps(L, X)
print("Longest Palindromic Subsequence:", lps)  # Output: carac
