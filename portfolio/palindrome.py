def ispalindrome(string):
    Left_pos=0
    right_pos=len(string) - 1
    while right_pos >= Left_pos:
        if not string[Left_pos] == string[right_pos]:
            return False
        Left_pos += 1
        right_pos -= 1
        return True
print("is it a palindrome?")
print(ispalindrome('madam'))