# mathematic = dict()
# informatic = dict()
# physics = dict()
# str = input()
# while(str!=""):
#     _str = str.split()
#     mathematic[_str[0]] = int(_str[1])
#     str = input()
#
# print(mathematic)
#
# while(str!=""):
#     _str = str.split()
#     informatic[_str[0]] = int(_str[1])
#     str = input()
#
# print(informatic)
#
# while(str!=""):
#     _str = str.split()
#     physics[_str[0]] = int(_str[1])
#     str = input()
# print(physics)

def fill_set():
    _set = dict()
    s = input()
    while (s != ""):
        _s = s.split()
        _set[_s[0]+s[1]] = int(_s[2])
        s=input()
    return _set

count = int(input())
_list_dict = [0]*count
for i in range(count):
    _list_dict[i] = fill_set()

for _set in _list_dict:
    print(_set)