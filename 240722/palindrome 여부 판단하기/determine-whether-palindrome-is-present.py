A = input()

def palindrome(string):
    for i in range(len(string)):
        if string[i] != A[i]:
            return False
    return True


if palindrome(A[::-1]):
    print("Yes")
else:
    print("No")