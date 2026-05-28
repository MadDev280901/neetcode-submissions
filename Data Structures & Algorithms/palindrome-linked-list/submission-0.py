class Solution:
    def isPalindrome(self, head):
        vals = []

        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        l, r = 0, len(vals) - 1

        while l < r:
            if vals[l] != vals[r]:
                return False

            l += 1
            r -= 1

        return True