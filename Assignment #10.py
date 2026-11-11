
import pandas as pd

# Read the CSV file and use Team as the index
df = pd.read_csv("cfb.csv", index_col="Team")

# Ask the user to enter a season
year = int(input("Enter a season to analyze: "))

# Keep asking the user until they enter a valid season
while year not in df["Season"].unique():
    print("Requested Season not found. Please select a valid year.")
    year = int(input("Enter a season to analyze: "))

# Create a dictionary to store teams in four win categories
results = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
}

# Filter the data to include only the selected season
selected_year = df[df["Season"] == year]

# Loop through each team in the selected season
for team, row in selected_year.iterrows():

    # Get the number of wins for the current team
    wins = int(row["Win"])

    # Place the team into the correct win category
    if wins >= 10:
        results["10 or more wins"].append(team)

    elif wins >= 8:
        results["8-9 wins"].append(team)

    elif wins >= 6:
        results["6-7 wins"].append(team)

    else:
        results["Fewer than 6 wins"].append(team)

# Display the selected season
print("College Football Results for", year)

# Loop through each category in the dictionary
for category, teams in results.items():

    # Print the category heading with a blank line before it
    print("\n" + category + ":")

    # Display every team in the current category
    for team in teams:
        print(team)
