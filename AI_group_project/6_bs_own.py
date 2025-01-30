import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set up the URL (replace with the actual URL you are scraping)
url = "https://www.google.com/search?q=epl+table"

# Set up headers to mimic a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

# Send a GET request to fetch the content
response = requests.get(url, headers=headers)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all 'tr' elements (rows in the EPL table)
rows = soup.find_all("tr", attrs={"aria-label": True})

# List to store extracted data
data_list = []

# Loop through each row and extract team info
for row in rows:
    # Extracting team name (from the 'aria-label' attribute)
    team_name = row['aria-label']
    
    # Extracting other table data using the 'td' elements
    data = row.find_all("td")
    
    # Extract the statistics from the columns
    games_played = data[3].get_text()
    wins = data[4].get_text()
    draws = data[5].get_text()
    losses = data[6].get_text()
    goals_for = data[7].get_text()
    goals_against = data[8].get_text()
    goal_diff = data[9].get_text()
    points = data[10].get_text()

    # Append extracted data to the list
    data_list.append([team_name, games_played, wins, draws, losses, goals_for, goals_against, goal_diff, points])

# Create a DataFrame from the list of data
df = pd.DataFrame(data_list, columns=["Team", "Games Played", "Wins", "Draws", "Losses", "Goals For", "Goals Against", "Goal Difference", "Points"])

# Save the DataFrame to an Excel file
df.to_excel("epl_table.xlsx", index=False)

print("Data has been written to epl_table.xlsx")
