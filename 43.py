class Pupils:
    def __init__(self,name,height):
        self.name=name
        self.height=height
        self.count+=1
    def __str__(self):
        print("Ім'я учасника:", self.name,"Зріст:", self.height)

p1=Pupils("Ігор",155)
p1.__str__()
p2=Pupils("Оля",158)
p2.__str__()
p3=Pupils("Яна",167)
p3.__str__()
print(p1.count,"Учасника змагань")