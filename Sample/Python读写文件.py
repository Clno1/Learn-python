import json

filename="username.json"

try:
    with open(filename) as f_obj:
        username=json.load(f_obj)
except FileNotFoundError:
    username=input("Please input your username:")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We will remember you, "+username+" !")
else:
    print("Welcome back, "+username+" !")
