import pandas as pd

def extract_data():
    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")

    return matches, deliveries