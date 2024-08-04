
def math(num1, num2):
    dict = {}
    dict['addition'] = num1 + num2
    dict['subtraction'] = num1 - num2
    dict['multiplication'] = num1 * num2

    return dict

response = math(33, 400)

print(response)
print(type(response))

print(response['multiplication'])