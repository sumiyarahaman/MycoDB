import pandas as pd
import matplotlib.pyplot as plt

fpath = 'MycoDB_version4.csv'

data = pd.read_csv(fpath)

experiment_means = data.groupby('EXPERIMENTID')['EFFECTSIZE1'].mean()

print(experiment_means.head())

# Group by PAPERYEAR and calculate summary statistics for EFFECTSIZE1
yearly_summary = data.groupby('PAPERYEAR')['EFFECTSIZE1'].describe()

print(yearly_summary.head())

# Plotting the mean EFFECTSIZE1 per year
yearly_means = data.groupby('PAPERYEAR')['EFFECTSIZE1'].mean()

plt.figure(figsize=(10, 6))
plt.plot(yearly_means.index, yearly_means.values, marker='o', linestyle='-')
plt.title('Mean Effect Size Over Years')
plt.xlabel('Year')
plt.ylabel('Mean Effect Size')
plt.grid(True)
plt.show()
