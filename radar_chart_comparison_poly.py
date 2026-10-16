import numpy as np
import matplotlib.pyplot as plt
from google.colab import files  # for automatic download in Colab

# ============================================================================
# Data for Polytechnics (based on the policy scores)
# ============================================================================
categories = [
    'Transparency',
    'Academic Integrity',
    'Clarity of AI Rules',
    'Ethics & Bias',
    'Data Privacy',
    'Equity & Access'
]

# Values for each polytechnic (in the same order as categories above)
data = {
    'OP': [3.0, 3.0, 3.0, 2.5, 2.5, 3.0],
    'Ara': [2.5, 3.0, 3.0, 2.0, 2.5, 2.5],
    'Wintec': [3.0, 3.5, 3.0, 2.5, 3.0, 3.0],
    'TO': [3.0, 3.5, 3.0, 2.5, 3.0, 3.0],
    'OtagoP': [2.0, 2.5, 2.0, 1.5, 2.0, 2.0],
    'SIT': [2.5, 3.0, 2.5, 2.0, 2.5, 2.5],
    'MIT': [3.0, 4.0, 3.5, 3.0, 3.5, 3.0],
    'Unitec': [3.0, 3.5, 3.0, 2.5, 3.0, 3.0],
    'W&W': [2.8, 3.0, 2.5, 2.0, 2.5, 2.5]
}

# Number of variables
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# ============================================================================
# Colour palette for different polytechnics
# ============================================================================
colours = [
    '#1f77b4',  # OP - blue
    '#ff7f0e',  # Ara - orange
    '#2ca02c',  # Wintec - green
    '#d62728',  # TO - red
    '#9467bd',  # OtagoP - purple
    '#8c564b',  # SIT - brown
    '#e377c2',  # MIT - pink
    '#7f7f7f',  # Unitec - grey
    '#bcbd22'   # W&W - yellow-green
]

# ============================================================================
# Create the radar chart
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each polytechnic
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
plt.savefig('Radar_Polytechnics.png', dpi=600, bbox_inches='tight')
plt.show()
files.download('Radar_Polytechnics.png')