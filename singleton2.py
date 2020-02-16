class Human:
    __instance=None
    def __init__(self,name):
        self.name=name

    def __new__(cls, *args, **kwargs):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
h1=Human('jack')

h2=Human('mike')

h2.sex='male'

print(h1.sex)

print(h1,h2)
