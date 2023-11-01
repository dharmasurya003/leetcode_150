
# 9. Palindrome Number | Easy

# Companies
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 


def isPalindrome(x: int) -> bool:
        str_x = str(x)
        i,j=0,len(str_x)-1
        while(j>= len(str_x)//2 ):
            if str_x[i]==str_x[j]:
                i+=1
                j-=1
            else:
                return False
        return True



if __name__ == '__main__':
     print(isPalindrome(121))
