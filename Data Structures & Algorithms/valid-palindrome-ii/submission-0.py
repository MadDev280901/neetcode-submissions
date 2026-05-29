class Solution:
    def validPalindrome(self, s: str) -> bool:

        memo = {}

        def f(l, r, b):
            if l >= r:
                return True
            else:
                if (l, r, b) in memo:
                    return memo[(l, r, b)]

                if s[l] != s[r]:
                    if b == 1:
                        memo[(l, r ,b)] = f(l, r-1, 0) | f(l+1, r, 0)
                        return memo[(l, r ,b)]
                
                    else:
                        memo[(l, r ,b)] = False
                        return memo[(l, r ,b)]
                
                else:
                    memo[(l, r, b)]  = f(l+1, r-1, b)
                    return memo[(l, r ,b)]

        return f(0, len(s)-1, 1)


        