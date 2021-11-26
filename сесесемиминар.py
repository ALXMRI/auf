mathematic = dict()
informatic = dict()
physics = dict()
str = input()
while(str!=""):
_str = str.split()
mathematic[_str[0]] = int(_str[1])
str = input()

print(mathematic)

while(str!=""):
_str = str.split()
informatic[_str[0]] = int(_str[1])
str = input()

print(informatic)

while(str!=""):
_str = str.split()
physics[_str[0]] = int(_str[1])
str = input()
print(physics)