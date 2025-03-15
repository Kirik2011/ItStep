class Pupils:
    count=0
    def __init__(self,name,height):
        self.name=name
        self.height=height
        Pupils.count+=1
    def __str__(self):
        print("Ім'я учасника:", self.name,"Зріст:", self.height)
    def __bool__(self):
        return self.name!=None
    def __len__(self):
        return self.height

p1=Pupils("Ігор",155)
p1.__str__()
p2=Pupils("Оля",158)
p2.__str__()
p3=Pupils("Яна",167)
p3.__str__()
print(p1.count,"Учасника змагань")
# print(p1.__bool__())
print(bool(p2))
# print(p3.__len__())
print(len(p3))