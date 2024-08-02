def math(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2

    return add, sub, mult

response = math(33, 400)

# print(response)
# print(type(response))

# print(response[1]) # returns subtraction of values -367

print(response[2]) # returns multiplication of values 13200