import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files  # for automatic download in Colab

# ============================================================================
# Data extracted from the table (as provided)
# ============================================================================
data = {
    'Institution': [
        'OP', 'Ara', 'Wintec', 'TO',
        'OtagoP', 'SIT', 'MIT', 'Unitec',
        'W&W', 'UO', 'UoW',
        'VUW', 'UoA', 'UC'
    ],
    'Transparency': [3.0, 2.5, 3.0, 3.0, 2.0, 2.5, 3.0, 3.0, 2.7, 1.75, 2.0, 1.5, 2.0, 1.75],
    'Academic Integrity': [3.0, 3.0, 3.5, 3.5, 2.5, 3.0, 4.0, 3.5, 3.0, 2.0, 2.5, 2.0, 2.5, 2.0],
    'Clarity of AI Rules': [3.0, 3.0, 3.0, 3.0, 2.0, 2.5, 3.5, 3.0, 2.5, 1.75, 2.3, 1.5, 2.0, 1.75],
    'Ethics & Bias': [2.5, 2.0, 2.5, 2.5, 1.5, 2.0, 3.0, 2.5, 2.0, 1.5, 1.75, 1.0, 2.0, 1.5],
    'Data Privacy': [2.5, 2.5, 3.0, 3.0, 2.0, 2.5, 3.5, 3.0, 2.5, 1.75, 2.0, 1.5, 2.0, 1.75],
    'Equity & Access': [3.0, 2.5, 3.0, 3.0, 2.0, 2.5, 3.0, 3.0, 2.5, 1.75, 2.0, 1.5, 2.5, 2.0]
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('Institution', inplace=True)

# ============================================================================
# Define colours for each dimension (matching the original figure)
# ============================================================================
dimension_colours = {
    'Transparency': '#1f77b4',      # blue
    'Academic Integrity': '#ff7f0e', # orange
    'Clarity of AI Rules': '#2ca02c', # green
    'Ethics & Bias': '#d62728',      # red
    'Data Privacy': '#9467bd',       # purple
    'Equity & Access': '#8c564b'     # brown
}

# ============================================================================
# Create the grouped bar chart
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width and positions
bar_width = 0.12
x = np.arange(len(df.index))

# Plot each dimension as a group of bars
for i, (dimension, colour) in enumerate(dimension_colours.items()):
    offset = (i - 2.5) * bar_width  # Center the groups
    bars = ax.bar(x + offset, df[dimension], bar_width,
                  label=dimension, color=colour, edgecolor='black', linewidth=0.8)

# Set x-axis ticks and labels (no rotation)
ax.set_xticks(x)
ax.set_xticklabels(df.index, fontsize=12, weight='bold', rotation=0)

# Set y-axis limits
ax.set_ylim(0, 5)

# Set y-axis tick labels
ax.set_yticklabels([0, 1, 2, 3, 4, 5], fontsize=12, weight='bold', rotation=0)

# Set y-axis label (x-axis label removed)
ax.set_ylabel('Score (1=Best, 5=Worst)', fontsize=16, weight='bold')
ax.set_xlabel('')  # Remove x-axis label

# Customise tick fonts
ax.tick_params(axis='y', labelsize=12)

# Add legend with larger font
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize=14, frameon=True)

# Add light grid for readability
ax.grid(axis='y', linestyle=':', alpha=0.5)

# ============================================================================
# ADD A SMALL SPACE ON BOTH SIDES OF THE BARS
# ============================================================================
ax.set_xlim(-0.5, len(df.index) - 0.5)  # small padding (0.5 on each side)

# Alternatively, you can use margins:
# ax.margins(x=0.03)

# Tight layout
plt.tight_layout()

# Save and download
plt.savefig('Grouped_bar.png', dpi=600, bbox_inches='tight')
plt.show()
files.download('Grouped_bar.png')