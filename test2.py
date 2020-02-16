class Person:

    def __init__(self, name, hp, aggr, sex):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.sex = sex

    def attack(self,dog):
        dog.hp -= self.aggr
        print("%s被%s 打了，损失了%s的血量"%(dog.name,self.name,self.aggr))

class Dog:

    def __init__(self, name, hp, aggr, kind):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.kind = kind

    def bite(self,person):
        person.hp -= self.aggr
        print("%s被%s 打了，损失了%s的血量"%(person.name, self.name, self.aggr))

alex = Person("alex liu",500,100,'male')

print(Person.__dict__)
print(alex.__dict__)

dog = Dog("goofy", 500, 300, 'teddy')
alex.attack(dog)

dog.bite(alex)
