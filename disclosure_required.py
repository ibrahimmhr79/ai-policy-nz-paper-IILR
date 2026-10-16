import matplotlib.pyplot as plt
from google.colab import files  # for automatic download in Colab

# Data
categories = ['No', 'Yes']
percentages = [78.6, 21.4]

# Colours: No = light grey, Yes = dark blue (to highlight)
colours = ['#d9d9d9', '#008080']

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Pie chart with custom colours and larger text
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=categories,
    autopct='%1.1f%%',
    colors=colours,
    startangle=90,
    textprops={'fontsize': 16, 'weight': 'bold'},
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Make percentage text larger and bolder
for autotext in autotexts:
    autotext.set_fontsize(18)
    autotext.set_weight('bold')
    autotext.set_color('black')

# Make category labels larger
for text in texts:
    text.set_fontsize(16)
    text.set_weight('bold')

# Ensure pie is a circle
ax.axis('equal')

# No title

# Save and download
plt.tight_layout()
plt.savefig('Disclosure_Required.png', dpi=600, bbox_inches='tight')
plt.show()
files.download('Disclosure_Required.png')