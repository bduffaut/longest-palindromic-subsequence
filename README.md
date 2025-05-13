# longest-palindromic-subsequence
Finds the Longest Palindromic Subsequence in a string using dynamic programming and LCS logic.



# Longest Palindromic Subsequence (LPS) using Dynamic Programming

This project implements a classic dynamic programming solution to find the **Longest Palindromic Subsequence (LPS)** in a given string.

## Problem Statement

Given a string X, the goal is to find the longest subsequence of X that is also a palindrome. A subsequence is a sequence derived by deleting some or no characters without changing the order of the remaining characters.

### Example

Input: `"character"`  
Output: `"carac"`  
Explanation: "carac" is the longest palindromic subsequence in "character".

## Approach

This solution uses a common trick: computing the Longest Common Subsequence (LCS) between the string and its reverse. The LCS of a string and its reverse gives the longest palindromic subsequence.

### Steps:
1. Reverse the input string to create a comparison string.
2. Build a 2D dynamic programming table L[i][j] where each entry contains the length of the LCS between X[0..i] and reverse(X)[0..j].
3. Reconstruct the LPS by tracing back through the DP table.

## How to Run

This is a simple Python script. To run:

```bash
python3 longest_palindromic_subsequence.py
```

### Output Example:

```
Longest Palindromic Subsequence: carac
```
