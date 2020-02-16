def Person(name, hp, aggr, sex):
    person={
        "name": name,
        'hp': hp,
        'aggr': aggr,
        'sex': sex
    }

    return person




def Dog(name, hp, aggr,kind):

    dog={
         "name": name,
        'hp': hp,
        'aggr': aggr,
        'kind':kind
    }

    return dog;

alex = Person('alex chang',1000,200,'male')
print(alex['hp'])

