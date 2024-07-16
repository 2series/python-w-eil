my_list = ['bob', 'sue', 'phil', 'bobby']

for x in my_list:
 print(x)

for x in my_list:
    if 'bob' in x:
        print(x)

my_dict = {'name':'frank', 'age':13, 'size':'large'}
print(my_dict['name'])

for key, value in my_dict.items():
    print(f'{key} = {value}')