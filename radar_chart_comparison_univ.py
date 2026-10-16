import numpy as np
import matplotlib.pyplot as plt
from google.colab import files  # for automatic download in Colab

# ============================================================================
# Data for Universities (based on the policy scores from the paper)
# ============================================================================
categories = [
    'Transparency',
    'Academic Integrity',
    'Clarity of AI Rules',
    'Ethics & Bias',
    'Data Privacy',
    'Equity & Access'
]

# Values for each university (in the same order as categories above)
data = {
    'UO': [1.8, 2.0, 1.8, 1.5, 1.8, 1.8],
    'UoW': [2.0, 2.5, 2.2, 1.8, 2.0, 2.0],
    'VUW': [1.5, 2.0, 1.5, 1.0, 1.5, 1.5],
    'UoA': [2.0, 2.5, 2.0, 2.0, 2.0, 2.5],
    'UC': [1.8, 2.0, 1.8, 1.5, 1.8, 2.0]
}

# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# ============================================================================
# Colour palette for different universities
# ============================================================================
colours = [
    '#1f77b4',  # UO - blue
    '#ff7f0e',  # UoW - orange
    '#2ca02c',  # VUW - green
    '#d62728',  # UoA - red
    '#9467bd'   # UC - purple
]

# ============================================================================
# Create the radar chart
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each university
for i, (name, values) in enumerate(data.items()):
    values += values[:1]  # Close the loop
    ax.plot(angles, values, linewidth=2.5, linestyle='-',
            color=colours[i % len(colours)], label=name)
    ax.fill(angles, values, alpha=0.15, color=colours[i % len(colours)])

# Set category labels with larger, bold font
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=14, weight='bold')

# Set y-axis ticks and labels
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=12)

# Add grid lines
ax.grid(True, linestyle=':', alpha=0.7)

# Add legend with larger font
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=12, frameon=True)

# Remove title
# No title

# Remove axis labels
# No xlabel or ylabel

# Tight layout
plt.tight_layout()

# Save and download
plt.savefig('Radar_Universities.png', dpi=600, bbox_inches='tight')
plt.show()
files.download('Radar_Universities.png')