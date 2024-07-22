n = int(input())

def print_world(n):
    if n == 0:
        return
    
    print_world(n-1)
    print("HelloWorld")

print_world(n)