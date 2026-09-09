class Solution(object):
    def isPalindrome(self, num):
        if num < 0:
            return False

        original = num
        reversed_num = 0

        while num > 0:
            last_digit = num % 10
            reversed_num = (reversed_num * 10) + last_digit
            num = num // 10

        return original == reversed_num


s = Solution()

print(s.isPalindrome(121))
print(s.isPalindrome(123))