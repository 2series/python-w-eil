import os

command = 'ls -l'
# command = 'ping -c 1 cnn.com' # -c is count, Return all lines 
# command = 'ping -c 1 cnn.com | grep packet' # returns only packet line(s)

response = os.popen(command).read()
# response = os.popen(command).readlines()

print(response)