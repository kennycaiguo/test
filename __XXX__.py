class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def __str__(self):
        return "Name:%s,age:%s,sex:%s"%(self.name,self.age,self.sex)

    def __getitem__(self, item):   #in order to be able use sex=p['sex'],have to implement this methd
        return self.__dict__[item]

    def __setitem__(self, key, value):
         self.__dict__[key]= value

    def __call__(self, *args, **kwargs):
        print('this is call method')

    def __len__(self):
         return len(self.__dict__)
    def __eq__(self, other):
        # if (self.name == other.name) and (self.age == other.age) and (self.sex == other.sex):
        #     return True
        # else:
        #     return False
        if self.__hash__()==other.__hash__():
            return True
        else:
            return False

    def __hash__(self):
         return  hash(self.name +self.sex)

p = Person('jack',25,'male')
p2 = Person('jack',25,'male')

print(p)

# print(p.__dict__)
print(p['sex'])
# p['sex']='female'
print(p==p2)
