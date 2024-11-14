import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'C:/Users/ASUS/OneDrive/Desktop/Caste based crime analysis/crime_by_state.csv'
crime_data = pd.read_csv(file_path)

# Group data by year for murders and assaults on women
yearly_murders = crime_data.groupby('Year')['Murder'].sum()
yearly_assaults = crime_data.groupby('Year')['Assault on women'].sum()

# Plot the line chart
plt.figure(figsize=(12, 6))
plt.plot(yearly_murders.index, yearly_murders.values, label='Murders', color='red', marker='o')
plt.plot(yearly_assaults.index, yearly_assaults.values, label='Assaults on Women', color='blue', marker='o')

# Chart details
plt.title('Trends of Murders and Assaults on Women by Year')
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()