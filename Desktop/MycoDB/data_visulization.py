import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the MycoDB data
fpath = 'MycoDB_version4.csv'

data = pd.read_csv(fpath)

# Visualize the effect size by plant family
sns.boxplot(x='PlantFamily', y='EFFECTSIZE1', data=data)
plt.xlabel('Plant family')
plt.ylabel('Effect size')
plt.title('Effect size by plant family')
plt.xticks(rotation=90)
plt.show()

# Visualize the effect size by fungal genus
sns.boxplot(x='FungalGenus', y='EFFECTSIZE1', data=data)
plt.xlabel('Fungal genus')
plt.ylabel('Effect size')
plt.title('Effect size by fungal genus')
plt.xticks(rotation=90)
plt.show()

# Visualize the effect size by plant life history
sns.boxplot(x='PLANTLIFEHISTORY', y='EFFECTSIZE1', data=data)
plt.xlabel('Plant History')
plt.ylabel('Effect size')
plt.title('Effect size by plant history')
plt.show()

# Visualize the effect size by mycorrhizal type
sns.boxplot(x='MYCORRHIZAETYPE', y='EFFECTSIZE1', data=data)
plt.xlabel('Mycorrhizal type')
plt.ylabel('Effect size')
plt.title('Effect size by mycorrhizal type')
plt.show()