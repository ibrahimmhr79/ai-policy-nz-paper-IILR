import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from google.colab import files  # for automatic download in Colab

# Data extracted from the table
data = {
    'Institution': [
        'OP', 'Ara', 'Wintec', 'TO',
        'OtagoP', 'SIT', 'MIT', 'Unitec',
        'W&W', 'UO', 'UoW',
        'VUW', 'UoA', 'UC'
    ],
    'Transparency': [3.0, 2.5, 3.0, 3.0, 2.0, 2.5, 3.0, 3.0, 2.8, 1.8, 2.0, 1.5, 2.0, 1.8],
    'Academic Integrity': [3.0, 3.0, 3.5, 3.5, 2.5, 3.0, 4.0, 3.5, 3.0, 2.0, 2.5, 2.0, 2.5, 2.0],
    'Clarity of AI Rules': [3.0, 3.0, 3.0, 3.0, 2.0, 2.5, 3.5, 3.0, 2.5, 1.8, 2.2, 1.5, 2.0, 1.8],
    'Ethics & Bias': [2.5, 2.0, 2.5, 2.5, 1.5, 2.0, 3.0, 2.5, 2.0, 1.5, 1.8, 1.0, 2.0, 1.5],
    'Data Privacy': [2.5, 2.5, 3.0, 3.0, 2.0, 2.5, 3.5, 3.0, 2.5, 1.8, 2.0, 1.5, 2.0, 1.8],
    'Equity & Access': [3.0, 2.5, 3.0, 3.0, 2.0, 2.5, 3.0, 3.0, 2.5, 1.8, 2.0, 1.5, 2.5, 2.0]
}

# Create DataFrame and set Institution as index
df = pd.DataFrame(data)
df.set_index('Institution', inplace=True)

# ============================================================================
# REMOVE THE INDEX NAME SO IT DOES NOT SHOW AS Y-AXIS LABEL
# ============================================================================
df.index.name = None

# ============================================================================
# Create a DARK BLUE → LIGHT BLUE → ORANGE → YELLOW colormap
# Direction now matches the paper caption:
#   Dark blue = 1 (strongest governance)
#   Yellow    = 5 (weakest governance)
# ============================================================================
colors = ['#08306b', '#2171b5', '#6baed6', '#fdae61', '#fee08b', '#ffff99']
cmap_custom = LinearSegmentedColormap.from_list('blue_yellow', colors, N=256)

# ============================================================================
# Create the heatmap
# ============================================================================
plt.figure(figsize=(12, 8))

ax = sns.heatmap(
    df,
    annot=True,
    fmt='.1f',
    cmap=cmap_custom,
    cbar=True,
    square=False,
    linewidths=0.5,
    annot_kws={'size': 14, 'weight': 'bold'},
    vmin=1.0,
    vmax=5.0          # <- FIX: full 1-5 scale, not 1-4
)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right', fontsize=14, weight='bold')
# Make y-axis tick labels horizontal (rotation=0)
plt.yticks(rotation=0, fontsize=14, weight='bold')

# Adjust colorbar label
cbar = ax.collections[0].colorbar
cbar.set_label('Score (1 = Strongest Governance, 5 = Weakest Governance)',
               fontsize=12, weight='bold')

# Adjust layout and save
plt.tight_layout()
plt.savefig('Heatmap_score_all_inst.png', dpi=600, bbox_inches='tight')
plt.show()

# Automatically download the file in Colab
files.download('Heatmap_score_all_inst.png')