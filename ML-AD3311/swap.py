def swap(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]
user_input = input("Enter a string: ")
result = swap(user_input)
print("String after swapping first and last characters:", result)
