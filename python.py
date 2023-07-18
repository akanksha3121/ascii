def new_string(s):
    ascii_val = [ord(c) for c in s]
    modified = [False for _ in s]
    
    for i in range(len(ascii_val)):
        if ascii_val[i] % 2 == 0:
            if i + 1 < len(ascii_val) and not modified[i+1]:
                ascii_val[i + 1] += ascii_val[i] % 7
                if ascii_val[i + 1] < 32 or ascii_val[i + 1] > 126:
                    ascii_val[i + 1] = 83
                modified[i + 1] = True
        else:
            if i - 1 >= 0 and not modified[i-1]:
                ascii_val[i - 1] -= ascii_val[i] % 5
                if ascii_val[i - 1] < 32 or ascii_val[i - 1] > 126:
                    ascii_val[i - 1] = 83
                modified[i - 1] = True
                
    result = ''.join(chr(c) for c in ascii_val)
    return result


# get user input
user_input = input("Enter a string: ")

# call the function with the user input
result = new_string(user_input)

# print the result
print(result)
