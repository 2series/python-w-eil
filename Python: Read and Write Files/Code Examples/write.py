data = input('Add a note: ')
with open('test.html', 'a') as file:
    # file.write(data) # no formatting
    # file.write(f'{data}\n') # with formatting \n
    # file.write(f'<p>{data}</p>') # formatting w/ <p> tags
    file.write(f'<h1>{data}</h1>\n') # ASCII text formatting
