class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = self.removeExtra(s)
        print(res)
        l = 0
        r = len(res) - 1
        while l <= r:
            if res[l] != res[r]:
                print(res[l], res[r])
                return False
            
            l += 1
            r -= 1
        return True

    def removeExtra(self, s):
        res = ''
        for i in range(len(s)):
            if s[i].isalnum():
                res += s[i].lower()
        return res

        