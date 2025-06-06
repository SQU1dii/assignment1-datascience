import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data from your image
data = {
    'Month': ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019'],
    'Searches': [50, 53, 59, 56, 62],
    'Direct': [39, 47, 42, 51, 51],
    'Social Media': [70, 80, 90, 87, 92]
}

df = pd.DataFrame(data)

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7)) # Adjust figure size as needed

bar_width = 0.25
index = np.arange(len(df['Month']))

# Create the bars
bar1 = ax.bar(index - bar_width, df['Searches'], bar_width, label='Searches', color='#4CAF50') # Example color: green
bar2 = ax.bar(index, df['Direct'], bar_width, label='Direct', color='#FF6347')   # Example color: red-orange
bar3 = ax.bar(index + bar_width, df['Social Media'], bar_width, label='Social Media', color='#FFD700') # Example color: gold

# Add value labels on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)

# Customize the plot
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Visitors in thousands', fontsize=12)
ax.set_title('Visitors by web traffic sources', fontsize=16)
ax.set_xticks(index)
ax.set_xticklabels(df['Month'], rotation=0) # Rotate if labels overlap
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=3) # Adjust legend position
ax.grid(axis='y', linestyle='--', alpha=0.7) # Add a horizontal grid for readability
ax.set_ylim(0, 110) # Set y-axis limit slightly above max value for labels

plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()
