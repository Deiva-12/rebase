import json

with open('abc.json', 'r') as file:
        data = json.load(file)
x=   data["a"]    
y=   data["b"]
print(x)
print(y)
print(x+y)