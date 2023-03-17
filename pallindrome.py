 Use the Reversed() function in Python to check if a String is a Palindrome

a_string = 'Was it a car or a cat I saw'

def palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    reversed_string = ''.join(reversed(a_string))
    return a_string == reversed_string

print(palindrome(a_string))

# Returns: True
