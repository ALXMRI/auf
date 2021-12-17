Mathematics_l = {}
Informatics_l = {}
Physics_l = {}

Mathematics_map = {}
Informatics_map = {}
Physics_map = {}

Mathematics_l = list(map(str,input().split()))
Informatics_l = list(map(str,input().split()))
Physics_l = list(map(str,input().split()))

def EnterDict(list, dict):
    k = 1
    for i in range(0,len(list)-1, 3):
        dict[str(k)+'_'+list[i+1][0]+'_'+str(len(list[i+1]))] = int(list[i+2])
        k += 1
    list.clear()
def PrintDict(dict):
    for i in dict:
        print(i)
def FindAndPrintAllOlimpiads(dict1, dict2, dict3):
    for i in dict1:
        if i in dict2 and i in dict3:
            print(i)
def FindAndPrintBestScore(dict1, dict2, dict3):
    _max = -1
    _maxItem = -1
    for i in dict1:
        if i in dict2 and i in dict3:
            if dict1.get(i)+dict2.get(i)+dict3.get(i) > _max:
                _max = dict1[i]+dict2[i]+dict3[i]
                _maxItem = i
    print(_maxItem, _max)

EnterDict(Mathematics_l, Mathematics_map)
EnterDict(Informatics_l, Informatics_map)
EnterDict(Physics_l, Physics_map)

print("В олимпиаде по математике приняли участие ", len(Mathematics_map), " уч.")
print("В олимпиаде по математике приняли участие ", len(Informatics_map), " уч.")
print("В олимпиаде по математике приняли участие ", len(Physics_map), " уч.")

print("Список учеников, которые поучавствовали в олимпиаде по математике")
PrintDict(Mathematics_map)
print("Список учеников, которые поучавствовали в олимпиаде по информатике")
PrintDict(Informatics_map)
print("Список учеников, которые поучавствовали в олимпиаде по физике")
PrintDict(Physics_map)

print("Список учеников, которые поучавствовали во всех олимпиадах:")
FindAndPrintAllOlimpiads(Mathematics_map, Informatics_map, Physics_map)

print("Ученик, который набрал наибольшее количество баллов:")
FindAndPrintBestScore(Mathematics_map, Informatics_map, Physics_map)