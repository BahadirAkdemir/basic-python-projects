import pandas as pd

data = pd.read_csv('central_park_squirrel_census/squirrel.csv')
#print(data["Primary Fur Color"])
black=data[data["Primary Fur Color"]=="Black"]
gray=data[data["Primary Fur Color"]=="Gray"]
cinnamon=data[data["Primary Fur Color"]=="Cinnamon"]

print(len(black))
print(len(gray))
print(len(cinnamon))

data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Number": [len(black), len(gray), len(cinnamon)]
}
pd.DataFrame(data_dict).to_csv('central_park_squirrel_census/squirrel_color.csv')