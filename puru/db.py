import pandas as pd

data = pd.read_csv("./data.csv", index_col="ingredient")
data[data.isna()] = ""

def harmful_level(ingredient):
    try:
        return data.loc[ingredient, "harmful_level"]
    except KeyError:
        return "1"

def comment(ingredient):
    try:
        return data.loc[ingredient, "comment"]
    except KeyError:
        return ""

def benefit(ingredient):
    try:
        return data.loc[ingredient, "benefit"]
    except KeyError:
        return []