import os

result = os.popen('ping -c 1 cnn.com').read()

print('---- RESULT ----')
print(result)

if '1 packets received' in result:
    print('Site is UP!!!!')    
else:
    print('Site is DOWN')