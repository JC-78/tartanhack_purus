import pandas as pd

data = pd.read_csv("./data.csv", index_col="ingredient")

def harmful_level(ingredient):
    return data.loc[ingredient, "harmful_level"]

def comment(ingredient):
    return data.loc[ingredient, "comment"]

def benefit(ingredient):
    return data.loc[ingredient, "benefit"]