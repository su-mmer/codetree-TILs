def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

a = input()
print("Yes") if is_palindrome(a) else print("No")