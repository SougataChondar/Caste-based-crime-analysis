import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the Dataset

crime_data=pd.read_csv('crime_by_district.csv')

# Setup the Plot Style

sns.set(style='whitegrid')
# Select columns related to crime counts

crime_columns = ['Murder', 'Assault on women', 'Kidnapping and Abduction',
                 'Dacoity', 'Robbery', 'Arson', 'Hurt',
                 'Prevention of atrocities (POA) Act',
                 'Protection of Civil Rights (PCR) Act',
                 'Other Crimes Against SCs']


# Group data by state and sum up crime counts (assuming there is a 'STATE' column)
total_crime_counts_by_state = crime_data.groupby('STATE/UT')[crime_columns].sum()

# Find the most common crime in each state
most_common_crime_per_state = total_crime_counts_by_state.idxmax(axis=1)
most_common_crime_counts_by_state = total_crime_counts_by_state.max(axis=1)

# Create a DataFrame for visualization
most_common_crime_state_df = pd.DataFrame({
    'Most Common Crime': most_common_crime_per_state,
    'Count': most_common_crime_counts_by_state
})

# Display the DataFrame to see which crime happened most in each state
print(most_common_crime_state_df)
# Plot the most common crime in each state
plt.figure(figsize=(16, 10))
bars = sns.barplot(
    x=most_common_crime_state_df.index, 
    y=most_common_crime_state_df['Count'], 
    hue=most_common_crime_state_df['Most Common Crime'], 
    dodge=False, 
    palette='magma'
)
# Customize the plot aesthetics
plt.title('Most Common Crime in Each State', fontsize=18, fontweight='bold')
plt.xlabel('State', fontsize=14)
plt.ylabel('Count of Most Common Crime', fontsize=14)
plt.xticks(rotation=75, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Crime Type', title_fontsize=13, fontsize=11)

# Add value annotations to the bars
for bar in bars.patches:
    bars.annotate(format(bar.get_height(), '.0f'),
                  (bar.get_x() + bar.get_width() / 2., bar.get_height()),
                  ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()



