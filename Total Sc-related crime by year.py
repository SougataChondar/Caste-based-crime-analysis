import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'C:/Users/ASUS/OneDrive/Desktop/Caste based crime analysis/crime_by_state.csv'
crime_data = pd.read_csv(file_path)

# Define the columns related to SC crimes
sc_crime_columns = [
    'Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
    'Arson', 'Hurt', 'Prevention of atrocities (POA) Act',
    'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs'
]

# Group by year and sum the relevant SC crime columns
yearly_sc_crimes = crime_data.groupby('Year')[sc_crime_columns].sum()

# Add a total column to get the sum of SC-related crimes per year
yearly_sc_crimes['Total_SC_Crimes'] = yearly_sc_crimes.sum(axis=1)

# Find the year with the maximum total SC crimes
max_sc_crime_year = yearly_sc_crimes['Total_SC_Crimes'].idxmax()
max_sc_crime_total = yearly_sc_crimes['Total_SC_Crimes'].max()

print(f"The year with the most SC-related crimes was {max_sc_crime_year} with {max_sc_crime_total} crimes.")

# Plotting the total SC-related crimes per year as a bar graph
plt.figure(figsize=(12, 6))
plt.bar(yearly_sc_crimes.index, yearly_sc_crimes['Total_SC_Crimes'], 
        color='darkblue')
plt.title('Total SC-Related Crimes by Year')
plt.xlabel('Year')
plt.ylabel('Total SC-Related Crimes')
plt.xticks(yearly_sc_crimes.index, rotation=45)
plt.tight_layout()

plt.show()







