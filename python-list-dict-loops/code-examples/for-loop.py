my_list = ['bob', 'sue', 'bobby', 'bo', 'tim', 'tommy']

my_dict = {'name':'bob', 'age':19, 'gender':'male', 'size':'xl'}

# for x in my_list: # iterates through elements in []
#     print(x)

# for name in my_list: # iterate through elements in []
    # if 'bob' in name:
        # print(name)

# for key, value in my_dict.items():
#     print(f'{key} - {value}') # dash is the operator, can be changed to = operator

for key, value in my_dict.items():
    print(f'{key.title()} - {str(value).upper()}')