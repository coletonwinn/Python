import pandas as pd

park_info = pd.read_csv("national_parks_sample.csv")

parkiloc = park_info.query(
    'Park == "Everglades"',
)    [["Park", "Region","TrailMiles"]]


print(parkiloc)
