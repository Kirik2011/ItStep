#Симулятор студента
import random


class Student:
    def __init__(self,name):
        self.name=name
        self.happy=random.randint(10,100)
        self.progress=random.randint(0,10)
        self.alive=True
    def study(self):
        print("Час для навчання")
        self.happy-=random.randint(1,50)
        self.progress+=random.randint(1,15)
    def sleep(self):
        print("Час для сну")
        self.happy += random.randint(1,10)
    def chill(self):
        print("Час відпочинку")
        self.happy+=random.randint(50,100)
        self.progress-=random.randint(5,10)
    def isAlive(self):
        if 1<self.progress<5:
            print("ВІДРАХУВАННЯ")
        elif self.progress <=1:
            print("ВІДРАХУВАННЯ")
        elif self.progress >= 5:
            print("Відмінно")
            self.alive = False
    def everyday(self):
        print("Рівень щястя", self.happy)
        print("Прогрес навчання", self.progress)
    def studylife(self,day):
        day="День"+str(day)
        print(day)
        res=random.randint(1,3)
        if res==1:
            self.study()
        elif res==2:
            self.chill()
        else:
            self.sleep()
        self.everyday()
        self.isAlive()

st1=Student("Олег")
#print(st1.progress)
print("Життя студента", st1.name)
for k in range(1,8):
    if st1.alive==False:
        break
    st1.studylife(k)