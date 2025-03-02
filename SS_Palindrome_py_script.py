def is_palindrome(s):
    return s == s[::-1]

# Example usage
word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


#Code 2: Using for loop

def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case insensitivity
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

# Example usage
word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
