import matplotlib.pyplot as plt
from google.colab import files  # for automatic download in Colab

# ============================================================================
# Data (ordered from lowest to highest score, i.e., best to worst governance)
# ============================================================================
institutions = [
    'VUW', 'UO', 'UC', 'OtagoP', 'UoW', 'UoA',
    'SIT', 'W&W', 'Ara', 'OP', 'Wintec', 'TO', 'Unitec', 'MIT'
]

# Estimated values based on the original figure
scores = [
    1.50,   # VUW
    1.78,   # UO
    1.82,   # UC
    2.00,   # OtagoP
    2.08,   # UoW
    2.17,   # UoA
    2.50,   # SIT
    2.55,   # W&W
    2.58,   # Ara
    2.83,   # OP
    3.00,   # Wintec
    3.00,   # TO
    3.00,   # Unitec
    3.33    # MIT
]

# ============================================================================
# Create the horizontal bar chart
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 7))

# Plot horizontal bars with a nice blue colour
bars = ax.barh(institutions, scores, color='#2171b5', height=0.6, edgecolor='black', linewidth=0.5)

# Add the score values at the end of each bar
ax.bar_label(bars, fmt='%.2f', padding=3, fontsize=13, weight='bold')

# Remove x-axis and y-axis labels
ax.set_xlabel('Institution',fontsize=14, weight='bold')
ax.set_ylabel('Average Governance Score (1 = Best, 5 = Worst)',fontsize=14, weight='bold')

# Remove the title
# No title is set

# Set x-axis limits to accommodate the values
ax.set_xlim(0, 4.0)

# Customise tick fonts
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)

# Add a light grid for readability
ax.grid(axis='x', linestyle=':', alpha=0.5)

# Tight layout
plt.tight_layout()

# Save at high resolution
plt.savefig('Average_governance_score.png', dpi=600, bbox_inches='tight')
plt.show()

# Automatically download the file in Colab
files.download('Average_governance_score.png')