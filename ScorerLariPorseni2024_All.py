

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
 
# Load the CSV file into a DataFrame
# df = pd.read_csv('c:/temp/ScorerLariPorseni2024_All.csv')
url = 'https://raw.githubusercontent.com/purawiraswanto/pythontest/main/ScorerLariPorseni2024_All.csv'
df = pd.read_csv(url) 
 
df['Time'] = pd.to_timedelta(df['Time'])
 
 
df['Minutes'] = df['Time'].dt.total_seconds() / 60
 
 
teams = df['Team'].unique()
genders = df['Gender'].unique()

 
plt.figure(figsize=(12, 8))
 
for team in teams:
    for gender in genders:
        team_gender_data = df[(df['Team'] == team) & (df['Gender'] == gender)]
        plt.plot(team_gender_data['Finisher'], team_gender_data['Minutes'], marker='o', linestyle='-', label=f"{team} - {gender}")
 
plt.xlabel('Finisher Position')
plt.xscale('linear')
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.grid
plt.ylabel('Time (minutes)')
plt.title('Finisher Position vs Time for Each Team and Gender')
plt.legend()
plt.grid(True)
plt.show()
