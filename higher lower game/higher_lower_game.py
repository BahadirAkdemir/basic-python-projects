#higher lower game
import random
objects=[
    {'name':'Kerem',
    'age':'31',
    'department':'Computer Engineering',
    'university':'Abdullah Gül University',
    'race':'Turkish',
    'class':3
    },
    {'name':'Gökçe',
    'age':'31',
    'department':'Electrical and Communication',
    'university':'Yıldız Technical University',
    'race':'Turkish',
    'class':4
    },
    {'name':'Şahane',
    'age':'22',
    'department':'Electrical and Electronical Engineering',
    'university':'Abdullah Gül University',
    'race':'Turkish',
    'class':5
    },
    {'name':'Yusuf',
    'age':'23',
    'department':'Computer Engineering',
    'university':'Abdullah Gül University',
    'race':'Turkish',
    'class':6
    },
    {'name':'Bahadır',
    'age':'20',
    'department':'Computer Engineering',
    'university':'Abdullah Gül University',
    'race':'Turkish',
    'class':1
    }

]

print("Higher or Lower?")
IsContinue=True
counter=0
while IsContinue:
    A=random.randint(1,len(objects)-1)
    B=random.randint(1,len(objects)-1)
    while A==B:
        B=random.randint(0,len(objects)-1)
    print(f"A:{objects[A]['name']},{objects[A]['department']},{objects[A]['university']},{objects[A]['race']},{objects[A]['class']} year student")
    print(f"B:{objects[B]['name']},{objects[B]['department']},{objects[B]['university']},{objects[B]['race']},{objects[B]['class']} year student")
    print("Which one is older?")
    userans = input()
    answer='A'
    if int(objects[A]['age'])< int(objects[B]['age']):
        answer = 'B'
    if userans==answer:
        counter+=1
    else:
        IsContinue=False