import pandas

data_read = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data = pandas.DataFrame(data_read)

Analysis_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [0, 0, 0]
}
Analysis = pandas.DataFrame(Analysis_dict)

for f_color in data["Primary Fur Color"]:
    Analysis.loc[Analysis["Fur Color"].isin([f_color]), "Count"] += 1
    # if f_color == "Gray":
    #     Analysis.loc[Analysis["Fur Color"].isin(f_color), "Count"] += 1
    # elif f_color == "Cinnamon":
    #     Analysis[Analysis.Fur_Color == "Cinnamon"].Count += 1
    # elif f_color == "Black":
    #     Analysis[Analysis.Fur_Color == "Black"].Count += 1
    # else:
    #     pass

print(Analysis)
Analysis.to_csv("squirrel_count.csv")
