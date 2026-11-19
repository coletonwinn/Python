
import pandas as pd

# VIDEO GAME CATALOG MANAGER

# Read the original CSV file
games = pd.read_csv("video_games_raw.csv")

print("VIDEO GAME CATALOG MANAGER")

# Ask the user which row to inspect
try:
    row_number = int(input("Enter a row number to inspect: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Check that the row number is valid
if row_number < 0 or row_number >= len(games):
    print("Invalid row number. Please run the program again.")

else:
    # Use .iloc[] to select a game by row position
    selected_game = games.iloc[row_number]

    print("\nSelected Game:")
    print("Title:", selected_game["Title"])
    print("Platform:", selected_game["Platform"])
    print("Genre:", selected_game["Genre"])
    print("Rating:", selected_game["Rating"])
    print("Current Status:", selected_game["Status"])

    # Ask the user for a new status
    new_status = input("\nEnter a new status (Backlog, Playing, Completed, or Dropped): ")

    # Use .at[] to update one specific game's status
    games.at[row_number, "Status"] = new_status

    # Add the Recommended column
    games["Recommended"] = "No"

    # Use .loc[] to update multiple rows that meet both conditions
    games.loc[
        (games["Rating"] >= 8) & (games["Price"] <= 40),
        "Recommended"
    ] = "Yes"

    # Use .query() to display recommended games
    recommended_games = games.query("Recommended == 'Yes'")

    print("\nRecommended Games:")
    print(recommended_games[["Title", "Platform", "Price", "Rating"]])

    # Save the updated catalog to a new CSV file
    games.to_csv("video_games_cleaned.csv", index=False)

    print("\nThe catalog has been updated.")
    print("Saved as video_games_cleaned.csv.")
